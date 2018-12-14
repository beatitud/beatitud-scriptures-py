from __future__ import unicode_literals
import re


class CanonBase:
    single_verse_re = {
        'en': 'v[.]*',
        'fr': 'v[.]*\s{0,2}',
    }

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

            self.single_verse_re_string = self.single_verse_re.get(self.language)

        # Otherwise we raise an error
        else:
            raise Exception('Text has no "books"')
