# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from scriptures.canons.base import CanonBase


class Canon(CanonBase):
    """
    Catholic Canonical Bible with Old and New Testaments
    """
    name = 'catholic'
    books = {
        # The Pentateuch
        'gn': {
            'en': ('Genesis', 'Gen', 'Gen(?:esis)?'),
            'fr': ('Genèse', 'Gn', 'Gen(?:èse)?'),
            'chapters':
                [31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35,
             46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26]
        },
        'ex': {
            'en': ('Exodus', 'Exod', 'Exod(?:us)?'),
            'fr': ('Exode', 'Exode', 'Exod(?:e)?'),
            'chapters':
                [22, 25, 22, 31, 23, 30, 25, 32, 35, 29, 10, 51, 22, 31, 27, 36, 16, 27, 25, 26, 36, 31, 33, 18, 40,
             37, 21, 43, 46, 38, 18, 35, 23, 35, 35, 38, 29, 31, 43, 38]
        },
        'lv': {
            'en': ('Leviticus', 'Lev', 'Lev(?:iticus)?'),
            'fr': ('Lévitique', 'Lev', 'Lév(?:itique)?'),
            'chapters':
                [17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24, 33, 44, 23, 55, 46, 34]
        },
        'nb': {
            'en': ('Numbers', 'Num', 'Num(?:bers)?'),
            'fr': ('Nombres', 'Nb', 'Nom(?:bres)?'),
            'chapters':
                [54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35, 41, 30, 25, 18, 65,
             23, 31, 40, 16, 54, 42, 56, 29, 34, 13]
        },
        'dt': {
            'en': ('Deuteronomy', 'Deut', 'Deut(?:eronomy)?'),
            'fr': ('Deutéronome', 'Deut', 'Deut(?:éronome)?'),
            'chapters':
                [46, 37, 29, 49, 33, 25, 26, 20, 29, 22, 32, 32, 18, 29, 23, 22, 20, 22, 21, 20, 23, 30, 25, 22, 19,
             19, 26, 68, 29, 20, 30, 52, 29, 12]
        },
        'jos': {
            'en': ('Joshua', 'Josh', 'Josh(?:ua)?'),
            'fr': ('Josué', 'Jos', 'Jos(?:ué)?'),
            'chapters':
                [18, 24, 17, 24, 15, 27, 26, 35, 27, 43, 23, 24, 33, 15, 63, 10, 18, 28, 51, 9, 45, 34, 16, 33]
        },
        'jg': {
            'en': ('Judges', 'Judg', 'Judg(?:es)?'),
            'fr': ('Juges', 'Jug', 'Jug(?:es)?'),
            'chapters':
                [36, 23, 31, 24, 31, 40, 25, 35, 57, 18, 40, 15, 25, 20, 20, 31, 13, 31, 30, 48, 25]
        },
        'rt': {
            'en': ('Ruth', 'Ruth', 'Ruth'),
            'fr': ('Ruth', 'Ruth', 'Ruth'),
            'chapters':
                [22, 23, 18, 22]
        },
        # The Historical Books
        '1s': {
            'en': ('I Samuel', '1 S', '(?:1|I)(?:\s)?Sam(?:uel)?'),
            'fr': ('I Samuel', '1 S', '(?:1|I)(?:\s)?Sam(?:uel)?'),
            'chapters':
                [28, 36, 21, 22, 12, 21, 17, 22, 27, 27, 15, 25, 23, 52, 35, 23, 58, 30, 24, 42, 15, 23, 29, 22, 44,
             25, 12, 25, 11, 31, 13]
        },
        '2s': {
            'en': ('II Samuel', '2 S', '(?:2|II)(?:\s)?Sam(?:uel)?'),
            'fr': ('II Samuel', '2 S', '(?:2|II)(?:\s)?Sam(?:uel)?'),
            'chapters':
                [27, 32, 39, 12, 25, 23, 29, 18, 13, 19, 27, 31, 39, 33, 37, 23, 29, 33, 43, 26, 22, 51, 39, 25]
        },
        '1kgs': {
            'en': ('I Kings', '1 Kgs', '(?:1|I)(?:\s)?K(?:in)?gs'),
            'fr': ('I Rois', '1 Rois', '(?:1|I)(?:\s)?R(?:ois)?'),
            'chapters':
                [53, 46, 28, 34, 18, 38, 51, 66, 28, 29, 43, 33, 34, 31, 34, 34, 24, 46, 21, 43, 29, 53]
        },
        '2kgs': {
            'en': ('II Kings', '2 Kgs', '(?:2|II)(?:\s)?K(?:in)?gs'),
            'fr': ('II Rois', '2 Rois', '(?:2|II)(?:\s)?R(?:ois)?'),
            'chapters':
                [18, 25, 27, 44, 27, 33, 20, 29, 37, 36, 21, 21, 25, 29, 38, 20, 41, 37, 37, 21, 26, 20, 37, 20, 30]
        },
        '1ch': {
            'en': ('I Chronicles', '1 Chr', '(?:1|I)(?:\s)?Chr(?:o(?:n(?:icles)?)?)?'),
            'fr': ('I Chroniques', '1 Chr', '(?:1|I)(?:\s)?Chr(?:o(?:n(?:iques)?)?)?'),
            'chapters':
                [54, 55, 24, 43, 26, 81, 40, 40, 44, 14, 47, 40, 14, 17, 29, 43, 27, 17, 19, 8, 30, 19, 32, 31, 31,
                 32, 34, 21, 30]
        },
        '2ch': {
            'en': ('II Chronicles', '2 Chr', '(?:2|II)(?:\s)?Chr(?:o(?:n(?:icles)?)?)?'),
            'fr': ('II Chroniques', '2 Chr', '(?:2|II)(?:\s)?Chr(?:o(?:n(?:iques)?)?)?'),
            'chapters':
                [17, 18, 17, 22, 14, 42, 22, 18, 31, 19, 23, 16, 22, 15, 19, 14, 19, 34, 11, 37, 20, 12, 21, 27, 28,
                 23, 9, 27, 36, 27, 21, 33, 25, 33, 27, 23]
        },
        'esd': {
            'en': ('Ezra', 'Ezra', 'Ezra'),
            'fr': ('Esdras', 'Esd', 'Esd(?:ras)?'),
            'chapters':
                [11, 70, 13, 24, 17, 22, 28, 36, 15, 44]
        },
        'ne': {
            'en': ('Nehemiah', 'Ne', 'Ne(?:hemiah)?'),
            'fr': ('Néhémie', 'Ne', 'N[ée](?:hémie)?'),
            'chapters':
                [11, 20, 32, 23, 19, 19, 73, 18, 38, 39, 36, 47, 31]
        },
        'tb': {
            'en': ('Tobit', 'Tb', 'Tob(?:it)?'),
            'fr': ('Tobie', 'Tb', 'Tob(?:ie)?'),
            'chapters':
                [22, 14, 17, 21, 22, 18, 17, 21, 6, 14, 18, 22, 18, 15]
        },
        'jdt': {
            'en': ('Judith', 'Jud', 'Jud(?:ith)?'),
            'fr': ('Judith', 'Jud', 'Jud(?:ith)?'),
            'chapters':
                [16, 28, 10, 15, 24, 21, 32, 36, 14, 23, 23, 20, 20, 19, 14, 25]
        },
        'est': {
            'en': ('Esther', 'Est', 'Est(?:her)?'),
            'fr': ('Esther', 'Est', 'Est(?:her)?'),
            'chapters':
                [22, 23, 15, 17, 14, 14, 10, 17, 32, 3]
        },
        '1m': {
            'en': ('I Maccabees', '1 M', '(?:1|I)(?:\s)?M(?:c(?:a(?:bees)?)?)?'),
            'fr': ('I Maccabées', '1 M', '(?:1|I)(?:\s)?M(?:c(?:a(?:bées)?)?)?'),
            'chapters':
                [63, 70, 59, 61, 68, 63, 50, 32, 73, 89, 74, 53, 53, 49, 41, 24]
        },
        '2m': {
            'en': ('II Maccabees', '2 M', '(?:2|II)(?:\s)?M(?:c(?:a(?:bees)?)?)?'),
            'fr': ('II Maccabées', '2 M', '(?:2|II)(?:\s)?M(?:c(?:a(?:bées)?)?)?'),
            'chapters':
                [36, 32, 40, 50, 27, 31, 42, 36, 29, 38, 38, 46, 26, 46, 39]
        },
        # The Wisdom Books
        'jb': {
            'en': ('Job', 'Jb', 'J(?:o)?b'),
            'fr': ('Job', 'Jb', 'J(?:o)?b'),
            'chapters':
                [22, 13, 26, 21, 27, 30, 21, 22, 35, 22, 20, 25, 28, 22, 35, 22, 16, 21, 29, 29, 34, 30, 17, 25, 6, 14,
                 23, 28, 25, 31, 40, 22, 33, 37, 16, 33, 24, 41, 30, 24, 34, 17]
        },
        'ps': {
            'en': ('Psalms', 'Ps', 'Ps(?:a)?(?:lm(?:s)?)?'),
            'fr': ('Psalms', 'Ps', 'Ps(?:a)?(?:ume(?:s)?)?'),
            'chapters':
                [6, 12, 8, 8, 12, 10, 17, 9, 20, 18, 7, 8, 6, 7, 5, 11, 15, 50, 14, 9, 13, 31, 6, 10, 22, 12, 14, 9, 11,
                 12, 24, 11, 22, 22, 28, 12, 40, 22, 13, 17, 13, 11, 5, 26, 17, 11, 9, 14, 20, 23, 19, 9, 6, 7, 23, 13,
                 11, 11, 17, 12, 8, 12, 11, 10, 13, 20, 7, 35, 36, 5, 24, 20, 28, 23, 10, 12, 20, 72, 13, 19, 16, 8, 18,
                 12, 13, 17, 7, 18, 52, 17, 16, 15, 5, 23, 11, 13, 12, 9, 9, 5, 8, 28, 22, 35, 45, 48, 43, 13, 31, 7,
                 10, 10, 9, 8, 18, 19, 2, 29, 176, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 18, 3, 3, 21, 26, 9, 8, 24, 13,
                 10, 7, 12, 15, 21, 10, 20, 14, 9, 6]
        },
        'pr': {
            'en': ('Proverbs', 'Pr', 'Pr(?:overbs)?'),
            'fr': ('Proverbes', 'Pr', 'Pr(?:overbes)?'),
            'chapters':
                [33, 22, 35, 27, 23, 35, 27, 36, 18, 32, 31, 28, 25, 35, 33, 33, 28, 24, 29, 30, 31, 29, 35, 34, 28,
                 28, 27, 28, 27, 33, 31]
        },
        'qo': {  # Ecclésiaste
            'en': ('Qohelet', 'Qo', 'Ecc(?:l(?:es(?:iastes)?)?)?|Qo(?:helet)?'),
            'fr': ('Qohélet (Ecclésiaste)', 'Qo', 'Ecc(?:l(?:es(?:iastes)?)?)?|Qo(?:helet)?'),
            'chapters':
                [18, 26, 22, 16, 20, 12, 29, 17, 18, 20, 10, 14]
        },
        'ct': {
            'en': ('The Song of Songs', 'Song', 'Song(?: of Sol(?:omon)?)?'),
            'fr': ('Cantique des Cantiques', 'Ct', 'C(?:an)?t(?:ique)?(?: des C(?:an)?t(?:iques)?)?'),
            'chapters':
                [17, 17, 11, 16, 16, 13, 13, 14]
        },
        'sg': {
            'en': ('Book of Wisdom', 'Wisdom', 'Book(?: of Wis(?:dom)?)?'),
            'fr': ('Sagesse de Salomon', 'Sg', 'S(?:a)?g(?:esse)?(?: de Sal(?:omon)?)?'),
            'chapters':
                [16, 24, 19, 20, 23, 25, 30, 21, 18, 21, 26, 27, 19, 31, 19, 29, 21, 25, 22]
        },
        'si': {  # Ecclésiastique
            'en': ('Sirach', 'Si', 'Ecc(?:l(?:es(?:iastes)?)?)?|Si(?:rach)?'),
            'fr': ('Siracide (Ecclésiastique)', 'Si', 'Ecc(?:l(?:[eé]s(?:iastiques)?)?)?|Si(?:racide)?'),
            'chapters':
                [30, 18, 31, 31, 15, 37, 36, 19, 18, 31, 34, 18, 26, 27, 20, 30, 32, 33, 30, 32, 28, 27, 28, 34, 26, 29,
                 30, 26, 28, 25, 31, 24, 32, 31, 26, 31, 31, 34, 35, 30, 22, 25, 33, 23, 26, 20, 25, 25, 16, 29, 30]
        },
        # The Prophetic Books
        'is': {
            'en': ('Isaiah', 'Is', 'Isa(?:iah)?'),
            'fr': ('Isaïe', 'Is', 'Is(?:a[ïi]e)?'),
            'chapters':
                [31, 22, 26, 6, 30, 13, 25, 22, 21, 34, 16, 6, 22, 32, 9, 14, 14, 7, 25, 6, 17, 25, 18, 23, 12, 21, 13,
                 29, 24, 33, 9, 20, 24, 17, 10, 22, 38, 22, 8, 31, 29, 25, 28, 28, 25, 13, 15, 22, 26, 11, 23, 15, 12,
                 17, 13, 12, 21, 14, 21, 22, 11, 12, 19, 12, 25, 24]
        },
        'jr': {
            'en': ('Jeremiah', 'Jr', 'Jer(?:emiah)?'),
            'fr': ('Jérémie', 'Jr', 'J(?:[ée])?r(?:émie)?'),
            'chapters':
                [19, 37, 25, 31, 31, 30, 34, 22, 26, 25, 23, 17, 27, 22, 21, 21, 27, 23, 15, 18, 14, 30, 40, 10, 38, 24,
                 22, 17, 32, 24, 40, 44, 26, 22, 19, 32, 21, 28, 18, 16, 18, 22, 13, 30, 5, 28, 7, 47, 39, 46, 64, 34]
        },
        'lm': {
            'en': ('Lamentations', 'Lm', 'Lam(?:entations)?'),
            'fr': ('Lamentations', 'Lm', 'Lam(?:entations)?'),
            'chapters':
                [22, 22, 66, 22, 22]
        },
        'ba': {
            'en': ('Baruch', 'Ba', 'Bar(?:uch)?'),
            'fr': ('Baruch', 'Ba', 'Bar(?:uch)?'),
            'chapters':
                [22, 35, 38, 37, 9, 72]
        },
        'ez': {
            'en': ('Ezekiel', 'Ez', 'Ezek(?:iel)?'),
            'fr': ('Ézéchiel', 'Ez', '[EÉ]z(?:[ée]chiel)?'),
            'chapters':
                [28, 10, 27, 17, 17, 14, 27, 18, 11, 22, 25, 28, 23, 23, 8, 63, 24, 32, 14, 49, 32, 31, 49, 27, 17, 21,
                 36, 26, 21, 26, 18, 32, 33, 31, 15, 38, 28, 23, 29, 49, 26, 20, 27, 31, 25, 24, 23, 35]
        },
        'dn': {
            'en': ('Daniel', 'Dn', 'D(?:a)?n(?:iel)?'),
            'fr': ('Daniel', 'Dn', 'D(?:a)?n(?:iel)?'),
            'chapters':
                [21, 49, 30, 37, 31, 28, 28, 27, 27, 21, 45, 13]
        },
        'os': {
            'en': ('Hosea', 'Hos', 'Hos(?:ea)?'),
            'fr': ('Osée', 'Os', 'Os(?:[ée]e)?'),
            'chapters':
                [11, 23, 5, 19, 15, 11, 16, 14, 17, 15, 12, 14, 16, 9]
        },
        'jl': {
            'en': ('Joel', 'Jl', 'J(?:oe)?l'),
            'fr': ('Joël', 'Jl', 'J(?:o[ëe])?l'),
            'chapters':
                [20, 32, 21]
        },
        'am': {
            'en': ('Amos', 'Am', 'Amos'),
            'fr': ('Amos', 'Am', 'Am(?:os)?'),
            'chapters':
                [15, 16, 15, 13, 27, 14, 17, 14, 15]
        },
        'ab': {
            'en': ('Obadiah', 'Obad', 'Obad(?:iah)?'),
            'fr': ('Abdias', 'Ab', 'Ab(?:dias)?'),
            'chapters':
                [21]
        },
        'jon': {
            'en': ('Jonah', 'Jon', 'Jon(?:ah)?'),
            'fr': ('Jonas', 'Jon', 'Jon(?:as)?'),
            'chapters':
                [17, 10, 10, 11]
        },
        'mi': {
            'en': ('Micah', 'Mi', 'Mi(?:cah)?'),
            'fr': ('Michée', 'Mi', 'Mi(?:ch[ée]e)?'),
            'chapters':
                [16, 13, 12, 13, 15, 16, 20]
        },
        'na': {
            'en': ('Nahum', 'Na', 'Na(?:hum)?'),
            'fr': ('Nahum', 'Na', 'Na(?:hum)?'),
            'chapters':
                [15, 13, 19]
        },
        'ha': {
            'en': ('Habakkuk', 'Ha', 'Ha(?:bakkuk)?'),
            'fr': ('Habaquq', 'Ha', 'Ha(?:baquq)?'),
            'chapters':
                [17, 20, 19]
        },
        'so': {
            'en': ('Zephaniah', 'Zeph', 'Zeph(?:aniah)?'),
            'fr': ('Sophonie', 'So', 'So(?:phonie)?'),
            'chapters':
                [18, 15, 20]
        },
        'ag': {
            'en': ('Haggai', 'Hag', 'Hag(?:gai)?'),
            'fr': ('Aggée', 'Ag', 'Ag(?:g[ée]e)?'),
            'chapters':
                [15, 23]
        },
        'za': {
            'en': ('Zechariah', 'Zech', 'Zech(?:ariah)?'),
            'fr': ('Zacharie', 'Za', 'Za(?:charie)?'),
            'chapters':
                [21, 13, 10, 14, 11, 15, 14, 23, 17, 12, 17, 14, 9, 21]
        },
        'ml': {
            'en': ('Malachi', 'Ml', 'M(?:a)?l(?:achi)?'),
            'fr': ('Malachie', 'Ml', 'M(?:a)?l(?:achie)?'),
            'chapters':
                [14, 17, 18, 6]
        },
        # The Gospels
        'mt': {
            'en': ('Matthew', 'Matt', 'Matt(?:hew)?'),
            'fr': ('Matthieu', 'Mt', 'M(?:a)?t(?:thieu)?'),
            'chapters':
                [25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75,
             66, 20]
        },
        'mc': {
            'en': ('Mark', 'Mark', 'Mark'),
            'fr': ('Marc', 'Mc', 'M(?:ar)?c'),
            'chapters':
                [45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20]
        },
        'lc': {
            'en': ('Luke', 'Luke', 'Luke'),
            'fr': ('Luc', 'Lc', 'L(?:u)?c'),
            'chapters':
                [80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53]
        },
        'jn': {
            'en': ('John', 'John', '(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I))John'),
            'fr': ('Jean', 'Jn', 'J(?:ea)?n'),
            'chapters':
                [51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25]
        },
        'ac': {
            'en': ('Acts', 'Acts', 'Acts'),
            'fr': ('Actes des apôtres', 'Ac', 'Ac(?:tes des ap[oô]tres)?'),
            'chapters':
                [26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28, 41, 40, 34, 28, 41, 38, 40, 30, 35, 27, 27,
                 32, 44, 31]
        },
        # New Testament Letters
        'rm': {
            'en': ('Romans', 'Rm', 'R(?:o)?m(?:ans)?'),
            'fr': ('Romains', 'Rm', 'R(?:o)?m(?:ains)?'),
            'chapters':
                [32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 23, 33, 27]
        },
        '1co': {
            'en': ('I Corinthians', '1 Co', '(?:1|I)(?:\s)?Co(?:rinthians)?'),
            'fr': ('I Corinthiens', '1 Co', '(?:1|I)(?:\s)?Co(?:rinthiens)?'),
            'chapters':
                [31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40, 58, 24]
        },
        '2co': {
            'en': ('II Corinthians', '2 Co', '(?:2|II)(?:\s)?Co(?:rinthians)?'),
            'fr': ('II Corinthiens', '2 Co', '(?:2|II)(?:\s)?Co(?:rinthiens)?'),
            'chapters':
                [24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14]
        },
        'ga': {
            'en': ('Galatians', 'Ga', 'Ga(?:latians)?'),
            'fr': ('Galates', 'Ga', 'Ga(?:lates)?'),
            'chapters':
                [24, 21, 29, 31, 26, 18]
        },
        'ep': {
            'en': ('Ephesians', 'Ep', 'Ep(?:hesians)?'),
            'fr': ('Éphésiens', 'Ep', '[EÉ]p(?:h[ée]siens)?'),
            'chapters':
                [23, 22, 21, 32, 33, 24]
        },
        'ph': {
            'en': ('Philippians', 'Ph', 'Ph(?:ilippians)?'),
            'fr': ('Philippiens', 'Ph', 'Ph(?:ilippiens)?'),
            'chapters':
                [30, 30, 21, 23]
        },
        'col': {
            'en': ('Colossians', 'Col', 'Col(?:ossians)?'),
            'fr': ('Colossiens', 'Col', 'Col(?:ossiens)?'),
            'chapters':
                [29, 23, 25, 18]
        },
        '1th': {
            'en': ('I Thessalonians', '1 Th', '(?:1|I)(?:\s)?Th(?:essalonians)?'),
            'fr': ('I Thessaloniciens', '1 Th', '(?:1|I)(?:\s)?Th(?:essaloniciens)?'),
            'chapters':
                [10, 20, 13, 18, 28]
        },
        '2th': {
            'en': ('II Thessalonians', '2 Th', '(?:2|II)(?:\s)?Th(?:essalonians)?'),
            'fr': ('II Thessaloniciens', '2 Th', '(?:2|II)(?:\s)?Th(?:essaloniciens)?'),
            'chapters':
                [12, 17, 18]
        },
        '1tm': {
            'en': ('I Timothy', '1 Tm', '(?:1|I)(?:\s)?T(?:i)?m(?:othy)?'),
            'fr': ('I Timothée', '1 Tm', '(?:1|I)(?:\s)?T(?:i)?m(?:oth[ée]e)?'),
            'chapters':
                [20, 15, 16, 16, 25, 21]
        },
        '2tm': {
            'en': ('II Timothy', '2 Tm', '(?:2|II)(?:\s)?T(?:i)?m(?:othy)?'),
            'fr': ('II Timothée', '2 Tm', '(?:2|II)(?:\s)?T(?:i)?m(?:oth[ée]e)?'),
            'chapters':
                [18, 26, 17, 22]
        },
        'tt': {
            'en': ('Titus', 'Tt', 'T(?:i)?t(?:us)?'),
            'fr': ('Tite', 'Tt', 'T(?:i)?t(?:e)?'),
            'chapters':
                [16, 15, 15]
        },
        'phm': {
            'en': ('Philemon', 'Phm', 'Phm|Phile(?:m(?:on)?)?'),
            'fr': ('Philémon', 'Phm', 'Phm|Phil[ée](?:m(?:on)?)?'),
            'chapters':
                [25]
        },
        'he': {
            'en': ('Hebrews', 'He', 'He(?:brews)?'),
            'fr': ('Hébreux', 'He', 'H[ée](?:breux)?'),
            'chapters':
                [14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40, 29, 25]
        },
        # The Catholic Letters
        'jc': {
            'en': ('James', 'Jas', 'Ja(?:me)?s'),
            'fr': ('Jacques', 'Jc', 'J(?:a)?c(?:ques)?'),
            'chapters':
                [27, 26, 18, 17, 20]
        },
        '1p': {
            'en': ('I Peter', '1 P', '(?:1|I)(?:\s)?Pet(?:er)?'),
            'fr': ('I Pierre', '1 P', '(?:1|I)(?:\s)?P(?:ierre)?'),
            'chapters':
                [25, 25, 22, 19, 14]
        },
        '2p': {
            'en': ('II Peter', '2 P', '(?:2|II)(?:\s)?Pet(?:er)?'),
            'fr': ('II Peter', '2 P', '(?:2|II)(?:\s)?P(?:ierre)?'),
            'chapters':
                [21, 22, 18]
        },
        '1jn': {
            'en': ('I John', '1 Jn', '(?:1|I)(?:\s)?J(?:oh)?n'),
            'fr': ('I Jean', '1 Jn', '(?:1|I)(?:\s)?J(?:ea)?n'),
            'chapters':
                [10, 29, 24, 21, 21]
        },
        '2jn': {
            'en': ('II John', '2 Jn', '(?:2|II)(?:\s)?J(?:oh)?n'),
            'fr': ('II Jean', '2 Jn', '(?:2|II)(?:\s)?J(?:ea)?n'),
            'chapters':
                [13]
        },
        '3jn': {
            'en': ('III John', '3 Jn', '(?:(?:3|III)(?:\s)?)J(?:oh)?n'),
            'fr': ('III Jean', '3 Jn', '(?:(?:3|III)(?:\s)?)J(?:ean)?n'),
            'chapters':
                [14]
        },
        'jude': {
            'en': ('Jude', 'Jude', 'Jude'),
            'fr': ('Jude', 'Jude', 'Jude'),
            'chapters':
                [25]
        },
        'ap': {
            'en': ('Revelation of Jesus Christ', 'Rev', 'Rev(?:elation)?(?:\sof Jesus Christ)?'),
            'fr': ('Apocalypse', 'Ap', 'Ap(?:ocalypse)?'),
            'chapters':
                [20, 29, 22, 11, 14, 17, 17, 13, 21, 11, 19, 17, 18, 20, 8, 21, 18, 24, 21, 15, 27, 21]
        },
    }
