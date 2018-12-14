from scriptures.canons import get_canon
from scriptures.reference import Reference, guess_partial_refs, simplify_refs
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
