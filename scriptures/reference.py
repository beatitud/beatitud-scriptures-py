from __future__ import unicode_literals
import re


class InvalidReferenceException(Exception):
    """
    Invalid Reference Exception
    """
    pass


class Reference:
    def __init__(self, book, chapter, verse=None, end_chapter=None, end_verse=None, canon=None):
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.end_chapter = end_chapter
        self.end_verse = end_verse
        self.language = canon.language
        self.canon = canon
        self.book_dict = None

    def __repr__(self):
        self.to_string()

    def normalize(self,):
        """
        Get a complete five value tuple scripture reference with full book name
        from partial data
        """
        # bn, c, v, ec, ev = self.normalize()

        if not self.book_dict:
            self.book_dict = self.find_book(self.book)

        # SPECIAL CASES FOR: BOOKS WITH ONE CHAPTER AND MULTI-CHAPTER REFERENCES

        # If the ref is in format: (Book, #, None, None, ?)
        # This is a special case and indicates a reference in the format: Book 2-3
        if self.chapter is not None and self.verse is None and self.end_chapter is None:
            # If there is only one chapter in this book, set the chapter to one and
            # treat the incoming chapter argument as though it were the verse.
            # This normalizes references such as:
            # Jude 2 and Jude 2-4
            if len(self.book_dict.get('chapters')) == 1:
                self.verse = self.chapter
                self.chapter = 1
            # If the ref is in format: (Book, ?, None, None, #)
            # This normalizes references such as: Revelation 2-3
            elif self.end_verse:
                self.verse = 1
                self.end_chapter = self.end_verse
                self.end_verse = None
        # If the ref is in the format (Book, #, None, #, #)
        # this is a special case that indicates a reference in the format Book 3-4:5
        elif self.chapter is not None and self.verse is None and self.end_chapter is not None:
            # The solution is to set the verse to one, which is what is
            # most likely intended
            self.verse = 1

        # Convert to integers or leave as None
        self.chapter = int(self.chapter) if self.chapter else None
        self.verse = int(self.verse) if self.verse else None
        self.end_chapter = int(self.end_chapter) if self.end_chapter else self.chapter
        self.end_verse = int(self.end_verse) if self.end_verse else None
        if not self.book_dict \
                or (self.chapter is None or self.chapter < 1 or self.chapter > len(self.book_dict.get('chapters'))) \
                or (self.verse is not None and (self.verse < 1 or self.verse >
                                                self.book_dict.get('chapters')[self.chapter - 1])) \
                or (self.end_chapter is not None and (
                self.end_chapter < 1
                or self.end_chapter < self.chapter
                or self.end_chapter > len(self.book_dict.get('chapters')))) \
                or (self.end_verse is not None and (
                self.end_verse < 1
                or (self.end_chapter and self.end_verse > self.book_dict.get('chapters')[self.end_chapter - 1])
                or (self.chapter == self.end_chapter and self.end_verse < self.verse))):
            raise InvalidReferenceException()

        if not self.verse:
            return self.book_dict.get(self.language)[0], self.chapter, 1, self.chapter, \
                   self.book_dict.get('chapters')[self.chapter - 1]
        if not self.end_verse:
            if self.end_chapter and self.end_chapter != self.chapter:
                self.end_verse = self.book_dict.get('chapters')[self.end_chapter - 1]
            else:
                self.end_verse = self.verse
        if not self.end_chapter:
            self.end_chapter = self.chapter
        return self.book_dict.get(self.language)[0], self.chapter, self.verse, self.end_chapter, self.end_verse

    def find_book(self, name):
        """
        Get a book from its name or None if not found
        """
        for book_dict in self.canon.books.values():
            if re.match('^%s$' % book_dict.get(self.language)[2], name, re.IGNORECASE):
                self.book_dict = book_dict
                return self.book_dict

        return None

    def is_valid(self,):
        """
        Check to see if a scripture reference is valid
        """
        try:
            return self.normalize() is not None
        except InvalidReferenceException:
            return False

    def to_string(self, ):
        """
        Get a display friendly string from a scripture reference
        """
        bn, c, v, ec, ev = self.normalize()

        if not self.book_dict:
            self.book_dict = self.find_book(bn)

        if c == ec and len(self.book_dict.get('chapters')) == 1:  # single chapter book
            if v == ev:  # single verse
                return '{0} {1}'.format(bn, v)
            else:  # multiple verses
                return '{0} {1}-{2}'.format(bn, v, ev)
        else:  # multi chapter book
            if c == ec:  # same start and end chapters
                if v == 1 and ev == self.book_dict.get('chapters')[c - 1]:  # full chapter
                    return '{0} {1}'.format(bn, c)
                elif v == ev:  # single verse
                    return '{0} {1}:{2}'.format(bn, c, v)
                else:  # multiple verses
                    return '{0} {1}:{2}-{3}'.format(
                        bn, c, v, ev)
            else:  # multiple chapters
                if v == 1 and ev == self.book_dict.get('chapters')[ec - 1]:  # multichapter ref
                    return '{0} {1}-{2}'.format(bn, c, ec)
                else:  # multi-chapter, multi-verse ref
                    return '{0} {1}:{2}-{3}:{4}'.format(bn, c, v, ec, ev)
