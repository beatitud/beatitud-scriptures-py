from __future__ import unicode_literals
from scriptures.canons.base import CanonBase


class Canon(CanonBase):
    """
    Deuterocanonical Books
    """
    name = 'deuterocanon'
    books = {
        'tob': {
            'en': ('Tobit', 'Tob', 'Tob(?:it)?'),
            'chapters': [22, 14, 17, 21, 22, 17, 18, 21, 6, 12, 19, 22, 18, 15]
        },
        'jdt': {
            'en': ('Judith', 'Jdt', 'Jud(?:ith)?'),
            'chapters': [16, 28, 10, 15, 24, 21, 32, 35, 14, 23, 23, 20, 20, 19, 13, 25]
        },
        'addesth': {
            'en': ('Additions to Esther', 'AddEsth', '(?:AddEsth|(?:Additions to|Rest of) Esther|Esther \\(Greek\\))'),
            'chapters': [39, 23, 22, 47, 28, 14, 10, 41, 32, 13]
        },
        'wis': {
            'en': ('The Wisdom of Solomon', 'Wis', '(?:The )?Wis(?:dom(?: of Solomon)?)?'),
            'chapters': [16, 24, 19, 20, 23, 25, 30, 20, 18, 21, 26, 27, 19, 31, 19, 29, 21,25, 22]
        },
        'sir': {
            'en': ('Sirach', 'Sir', 'Sir(?:ach)?|Ecclesiasticus'),
            'chapters': [30, 18, 31, 31, 15, 37, 36, 19, 18, 31, 34, 18, 26, 27, 20, 30, 32, 33, 30, 31, 28, 27, 34, 26, 29, 30,
                    26, 28, 25, 31, 24, 31, 26, 20, 26, 31, 34, 35, 30, 23, 25, 33, 23, 26, 20, 25, 25, 16, 29, 30]
        },
        'bar': {
            'en': ('Baruch', 'Bar', 'Bar(?:uch)?'),
            'chapters': [
                    21, 35, 37, 37, 9
                ]
        },
        'epjer': {
            'en': ('Letter of Jeremiah', 'EpJer', 'EpJer|Letter of Jeremiah'),
            'chapters': [73]
        },
        'prazar': {
            'en': ('Prayer of Azariah', 'prazar', '(?:prayer of |Pr)?Azar(?:iah)?|Song of (?:the )?Three Children'),
            'chapters': [68]
        },
        'sus': {
            'en': ('Susanna', 'susanna', '(?:Story of )?sus(?:anna)?'),
            'chapters': [64]
        },
        'bel': {
            'en': ('Bel and the Dragon', 'bel','bel(?:(?: and the)? dragon)?'),
            'chapters': [42]
        },
        '1macc': {
            'en': ('I Maccabees', '1Macc', '(?:1|I) ?Macc(?:abees)?'),
            'chapters': [64, 70, 60, 61, 68, 63, 50, 32, 73, 89, 74, 53, 53, 49, 41, 24]
        },
        '2macc': {
            'en': ('II Maccabees', '2Macc', '(?:2|II) ?Macc(?:abees)?'),
            'chapters': [36, 32, 40, 50, 27, 31, 42, 36, 29, 38, 38, 45, 26, 46, 39]
        },
    }
