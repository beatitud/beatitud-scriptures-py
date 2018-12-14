from __future__ import unicode_literals
import re
from scriptures.canons import get_canon


class InvalidReferenceException(Exception):
    """
    Invalid Reference Exception
    """
    pass


class Reference:
    def __init__(self, book=None, chapter=None, verse=None, end_chapter=None, end_verse=None, canon='catholic',
                 language='fr'):
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

    def __str__(self):
        b, c, v, ec, ev = self.book, self.chapter, self.verse, self.end_chapter, self.end_verse
        bc = self.book_code
        if not self.is_validated:
            raise InvalidReferenceException

        if ec != c:
            return '{}_{}-{}_{}-{}'.format(bc, c, ec, v, ev)

        if ev != v:
            return '{}_{}_{}-{}'.format(bc, c, v, ev)

        return '{}_{}_{}'.format(bc, c, v)

    def __repr__(self):
        b, c, v, ec, ev, bc = self.book, self.chapter, self.verse, self.end_chapter, self.end_verse, self.chapters
        if not b:
            b = 'Unknown'
            c = '___'
            return '<Ref({0} {1}:{2})>'.format(b, c, v)

        if c == ec and len(bc) == 1:  # single chapter book
            if v == ev:  # single verse
                return '<Ref({0} {1})>'.format(b, v)
            else:  # multiple verses
                return '<Ref({0} {1}-{2})>'.format(b, v, ev)
        else:  # multi chapter book
            if c == ec:  # same start and end chapters
                if v == 1 and ev == bc[c - 1]:  # full chapter
                    return '<Ref({0} {1})>'.format(b, c)
                elif v == ev:  # single verse
                    return '<Ref({0} {1}:{2})>'.format(b, c, v)
                else:  # multiple verses
                    return '<Ref({0} {1}:{2}-{3})>'.format(
                        b, c, v, ev)
            else:  # multiple chapters
                if v == 1 and ev == bc[ec - 1]:  # multi chapter ref
                    return '<Ref({0} {1}-{2})>'.format(b, c, ec)
                else:  # multi-chapter, multi-verse ref
                    return '<Ref({0} {1}:{2}-{3}:{4})>'.format(b, c, v, ec, ev)

    def validate(self, raise_error=True):
        """
        Get a complete five value tuple scripture reference with full book name
        from partial data
        """
        if not self.book_code:
            if not self.find_book(self.book):
                self.is_validated = False
                if not raise_error:
                    return self.is_validated
                raise InvalidReferenceException

        # Convert to integers or leave as None
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

        # In case of incomplete or wrong information, we raise an exception
        chapters_count = len(self.chapters)
        if (not self.chapter or self.chapter < 1 or self.chapter > chapters_count) \
                or (self.verse and (self.verse < 1 or self.verse > self.chapters[self.chapter - 1])) \
                or (self.end_chapter and (self.end_chapter < 1 or self.end_chapter < self.chapter or self.end_chapter > chapters_count)) \
                or (self.end_verse and (not self.verse or self.end_verse < 1 or (self.end_chapter and self.end_verse > self.chapters[self.chapter - 1])
                                        or (self.chapter == self.end_chapter and self.end_verse < self.verse))):
            self.is_validated = False
            if not raise_error:
                return self.is_validated
            raise InvalidReferenceException

        # When there are no values, we set default ones
        if not self.verse:
            self.verse = 1

        # If no end_verse is detected
        if not self.end_verse:
            # If an end_chapter is detected, then we assign as end verse the last verse of this end chapter
            if self.end_chapter and self.end_chapter != self.chapter:
                self.end_verse = self.chapters[self.chapter - 1]
            # Else we assign the first verse itself
            else:
                self.end_verse = self.verse

        # If no end chapter, we assign the start chapter
        if not self.end_chapter:
            self.end_chapter = self.chapter

        self.is_validated = True
        return self.is_validated

    def find_book(self, name):
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


def guess_partial_refs(refs):
    new_refs = list()
    for i, ref in enumerate(refs):
        # We try to guess refs where we only have a verse number
        if not ref.is_validated and not ref.book and not ref.chapter:
            index = 0
            while not ref.is_validated and index < i:
                ref.book = refs[index].book
                ref.chapter = refs[index].chapter
                ref.validate(raise_error=False)
                index += 1

        if ref.is_validated:
            new_refs.append(ref)

    return new_refs


def simplify_refs(refs):
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
