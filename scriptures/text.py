from scriptures.canons import get_canon
from scriptures.reference import Reference
import re


class Text:
    def __init__(self, text, language='en', canon='catholic'):
        self.canon = get_canon(canon)(language=language)
        self.language = language
        self.text = text
        self.references = None

        # We set the compiled regex to extract refs in text
        self.scripture_re = re.compile(
            r'\b(?P<book>%s)\s*'
            r'(?P<chapter>\d{1,3})'
            r'(?:\s*[:,]\s*(?P<verse>\d{1,3}))?'
            r'(?:\s*[-]\s*'
            r'(?P<end_chapter>\d{1,3}(?=\s*:\s*))?'
            r'(?:\s*:\s*)?'
            r'(?P<end_verse>\d{1,3})?'
            r')?'
            r'|\b%s(?P<single_verse>\d{1,3})\s*(?:\s*[-]\s*(?P<single_verse_end>\d{1,3}))?'
            % (self.canon.book_re_string, self.canon.single_verse_re_string), re.IGNORECASE | re.UNICODE)

    def __repr__(self):
        return self.text

    def extract_refs(self, guess=True, simplify=True):
        """
        Extract a tuple of bible references from text
        """
        self.references = list()
        for r in re.finditer(self.scripture_re, self.text):
            ref_params = r.groupdict()
            if not ref_params.get('verse'):
                ref_params['verse'] = ref_params.pop('single_verse', None)
            if not ref_params.get('end_verse'):
                ref_params['end_verse'] = ref_params.pop('single_verse_end', None)
            ref_params.pop('single_verse', None)
            ref_params.pop('single_verse_end', None)
            ref_params['canon'] = self.canon.name
            ref_params['language'] = self.language
            ref = Reference(**ref_params)
            ref.validate(raise_error=False)
            self.references.append(ref)

        if guess:
            self.references = guess_partial_refs(self.references)

        if simplify:
            self.references = simplify_refs(self.references)

        return self.references


def guess_partial_refs(refs):
    new_refs = list()
    for i, ref in enumerate(refs):
        # We try to guess refs where we only have a verse number
        if not ref.is_valid and not ref.book and not ref.chapter:
            index = 0
            while not ref.is_valid and index < i:
                ref.book = refs[index].book
                ref.chapter = refs[index].chapter
                ref.validate(raise_error=False)
                index += 1

        if ref.is_valid:
            new_refs.append(ref)

    return new_refs


def simplify_refs(refs):
    # We write our covering dict of arrays
    refs_dict = dict()
    for i, ref in enumerate(refs):
        # We cannot work on invalid refs
        if not ref.is_valid:
            continue
        # If book not already known, we initialise it
        if not refs_dict.get(ref.book):
            refs_dict[ref.book] = list([[0 for i in range(chapter)] for chapter in ref.chapters])

        for c in range(ref.end_chapter - ref.chapter + 1):
            for v in range(ref.end_verse - ref.verse + 1):
                refs_dict[ref.book][ref.chapter + c][ref.verse + v] = 1

    new_refs = list()
    # We read our covering dict
    for book, ref_list in refs_dict.items():
        ref = None
        for c, c_list in enumerate(ref_list):
            for v, value in enumerate(c_list):
                if value == 1 and not ref:
                    ref = Reference(book=book, chapter=c, end_chapter=c, verse=v, end_verse=v)
                    ref.validate()
                if value == 1 and ref:
                    ref.end_chapter = c + 1
                    ref.end_verse = v + 1
                if value == 0 and ref:
                    new_refs.append(ref)
                    ref = None

    return new_refs
