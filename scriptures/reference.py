from __future__ import unicode_literals
import re
from scriptures.canons import get_canon


class InvalidReferenceException(Exception):
    """
    Invalid Reference Exception
    """
    pass


class Reference:
    def __init__(self, text=None, book=None, chapter=None, verse=None, end_chapter=None,
                 end_verse=None, canon='catholic', language='fr'):
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.end_chapter = end_chapter
        self.end_verse = end_verse
        self.language = language
        self.canon = get_canon(canon)(language=language)
        self.book_code = None
        self.chapters = None
        self.is_validated = None
        if text:
            self.from_string(text)

    def __str__(self):
        return self.to_string(full_name=False, repr=False)

    def __repr__(self):
        return self.to_string(full_name=True, repr=True)

    def to_string(self, full_name=False, repr=False):
        b, c, v, ec, ev, bc = self.book_code if not full_name else self.book, self.chapter, \
                              self.verse, self.end_chapter, self.end_verse, self.chapters

        # If unknown book
        if not b:
            b = 'Unknown'
            c = '___'
            string = '{0} {1}:{2}'.format(b, c, v)

        # If book containing a single chapter
        elif c == ec and len(bc) == 1:
            if v == ev:  # single verse
                string = '{0} {1}'.format(b, v)
            else:  # multiple verses
                string = '{0} {1}-{2}'.format(b, v, ev)

        # If book containing more than one chapter
        else:
            # If described verses are in the same chapter
            if c == ec:
                # If no verses
                if not v:
                    string = '{0} {1}'.format(b, c)
                # If verses are covering the whole chapter
                elif v == 1 and ev == bc[c - 1]:
                    string = '{0} {1}'.format(b, c)
                # If single verse
                elif v == ev:  # single verse
                    string = '{0} {1}:{2}'.format(b, c, v)
                # If multiple verses
                else:
                    string = '{0} {1}:{2}-{3}'.format(b, c, v, ev)

            # If described verses are across multiple chapters
            else:
                if v == 1 and ev == bc[ec - 1]:  # multi chapter ref
                    string = '{0} {1}-{2}'.format(b, c, ec)
                else:  # multi-chapter, multi-verse ref
                    string = '{0} {1}:{2}-{3}:{4}'.format(b, c, v, ec, ev)

        if not full_name:
            string = string.replace(' ', '_')

        if repr:
            string = '<Ref({})>'.format(string)

        return string

    def from_string(self, string):
        # We try to extract ref from string
        from .text import Text
        t = Text(string, language=self.language, canon=self.canon.name)
        refs = t.extract_refs(guess=False, simplify=False)

        # If we don't find exactly one ref, we raise an error
        if not len(refs) == 1:
            raise InvalidReferenceException

        # Else, we use the ref we found, import params, and validate it
        ref = refs[0]
        self.book, self.chapter, self.verse, self.end_chapter, self.end_verse = \
            ref.book, ref.chapter, ref.verse, ref.end_chapter, ref.end_verse
        self.validate(raise_error=True)

    def validate(self, raise_error=True):
        """
        Serialize reference with specified canon: retrieve book name, control chapter and verse numbers, ...
        """

        # If no book code, we try to retrieve announced book
        if not self.book_code:
            if not self.__find_book(self.book):
                self.is_validated = False
                if not raise_error:
                    return self.is_validated
                raise InvalidReferenceException

        # We convert to integers or leave as None
        try:
            self.chapter = int(self.chapter) if self.chapter else None
            self.verse = int(self.verse) if self.verse else None
            self.end_chapter = int(self.end_chapter) if self.end_chapter else self.chapter
            self.end_verse = int(self.end_verse) if self.end_verse else None
        except Exception:
            self.is_validated = False
            if not raise_error:
                return self.is_validated
            raise InvalidReferenceException

        b, c, v, ec, ev, bc = self.book, self.chapter, \
                              self.verse, self.end_chapter, self.end_verse, self.chapters

        # If there is no chapter number, or an invalid chapter number
        # Or if there is an invalid verse number
        # Or if there is an invalid end verse number
        # Or if there is an invalid end chapter number
        # We raise an error
        if (not c or c < 1 or c > len(bc)) \
                or (v and (v < 1 or v > bc[c - 1])) \
                or (ec and (ec < 1 or ec < c or ec > len(bc))) \
                or (ev and (not v or ev < 1 or (ec and ev > bc[ec - 1]) or (c == ec and ev < v))):
            self.is_validated = False
            if not raise_error:
                return self.is_validated
            raise InvalidReferenceException

        # If no end chapter, we assign chapter itself
        if not ec:
            self.end_chapter = c
            ec = self.end_chapter

        # If there is no verse number, we assume that the whole chapter is pointed  out, and
        # we assign 1 to the verse, and the last verse of the last chapter to the end verse
        if not v:
            self.verse = 1
            self.end_verse = bc[ec - 1]
            v = self.verse
            ev = self.end_verse

        # Else if no end verse is specified, we assign the first verse itself
        elif not ev:
            self.end_verse = v

        self.is_validated = True
        return self.is_validated

    def __find_book(self, name):
        """
        Get a book from its name or None if not found
        """
        if not name:
            return None

        for book_code, book_dict in self.canon.books.items():
            if re.match('^%s$' % book_dict.get(self.language)[2], name, re.IGNORECASE):
                self.book = book_dict.get(self.language)[0]
                self.book_code = book_code
                self.chapters = book_dict.get('chapters')
                return self.book

        return None

    def is_valid(self,):
        """
        Check to see if a scripture reference is valid
        """
        try:
            return self.validate()
        except InvalidReferenceException:
            return False


def simplify_refs(refs):
    """
    Simplify redundant references list, like for instance [Ref("Mt 6, 3-4"), Ref("Mt 6, 5-7")] should
    be [Ref("Mt 6, 3-7")]
    :param refs: list of Reference objects
    :return: simplified list of Reference objects
    """
    # We write our covering dict of arrays
    refs_dict = dict()
    for i, ref in enumerate(refs):
        # We cannot work on invalid refs
        if not ref.is_validated:
            continue
        # If book not already known, we initialise it
        if not refs_dict.get(ref.book):
            refs_dict[ref.book] = list([[0 for i in range(verse_count)] for verse_count in ref.chapters])

        for c in range(ref.end_chapter - ref.chapter + 1):
            end_verse = ref.end_verse if ref.chapter + c == ref.end_chapter else ref.chapters[ref.chapter + c - 1]
            for v in range(end_verse - ref.verse + 1):
                refs_dict[ref.book][ref.chapter + c - 1][ref.verse + v - 1] = 1

    new_refs = list()
    # We read our covering dict
    for book, ref_list in refs_dict.items():
        ref = None
        for c, c_list in enumerate(ref_list):
            for v, value in enumerate(c_list):
                if value == 1 and not ref:
                    ref = Reference(book=book, chapter=c+1, end_chapter=c+1, verse=v+1, end_verse=v+1)
                    ref.validate(raise_error=False)
                if value == 1 and ref:
                    ref.end_chapter = c + 1
                    ref.end_verse = v + 1
                if value == 0 and ref:
                    if ref.is_valid():
                        new_refs.append(ref)
                    ref = None

    return new_refs
