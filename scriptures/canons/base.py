from __future__ import unicode_literals
import re


class CanonBase:
    def __init__(self, language='en'):
        self.language = language

        # We check for books
        if hasattr(self, 'books'):
            # We it is not a dictionary, we raise an error
            if not isinstance(self.books, dict):
                raise Exception('"books" should be a dictionary, who\'s values are four valued tuples (Book Name, '
                                'Abbreviation, Regex, [ch1_verse_count, ch2_verse_count, ...])')

            # We set the regex instance variables
            self.book_re_string = '|'.join(b.get(self.language)[2] for b in self.books.values())
            self.book_re = re.compile(self.book_re_string, re.IGNORECASE | re.UNICODE)

            # We set the compiled scripture reference regex
            self.scripture_re = re.compile(
                r'\b(?P<BookTitle>%s)\s*'
                r'(?P<ChapterNumber>\d{1,3})'
                r'(?:\s*:\s*(?P<VerseNumber>\d{1,3}))?'
                r'(?:\s*[-\u2013\u2014]\s*'
                r'(?P<EndChapterNumber>\d{1,3}(?=\s*:\s*))?'
                r'(?:\s*:\s*)?'
                r'(?P<EndVerseNumber>\d{1,3})?'
                r')?' % (self.book_re_string,), re.IGNORECASE | re.UNICODE)

        # Otherwise we raise an error
        else:
            raise Exception('Text has no "books"')

    def get_book(self, name):
        """
        Get a book from its name or None if not found
        """
        for book in self.books.values():
            if re.match('^%s$' % book.get(self.language)[2], name, re.IGNORECASE):
                return book

        return None
