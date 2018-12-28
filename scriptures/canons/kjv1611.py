from __future__ import unicode_literals
from scriptures.canons.base import CanonBase
from .protestant import Canon as ProtestantCanon
from .deuterocanon import Canon as Deuterocanon


class Canon(CanonBase):
    """
    KingJames1611 - Contains what is considered the protestant canonical texts,
    plus the Deuteronomical books (in its Apocrypha)
    plus its additional Apocryphal books (I and II Esdras)
    """
    name = 'kjv1611'
    books = {}
    books.update(ProtestantCanon.books)
    books.update(Deuterocanon.books)
    books.update({
        '1esd': {
            'en': ('I Esdras', '1Esd', '(?:(?:1|I)(?:\s)?)Esd(?:ras)?'),
            'chapters': [58, 30, 24, 63, 73, 34, 15, 96, 55]
        },
        '2esd': {
            'en': ('II Esdras', '2Esd', '(?:(?:2|II)(?:\s)?)Esd(?:ras)?'),
            'chapters': [40, 48, 36, 52, 56, 59, 70, 63, 47, 59, 46, 51, 58, 48, 63, 78]
        },
        'prman': {
            'en': ('Prayer of Manasseh', 'prman', 'prman|(?:prayer of )?manasseh'),
            'chapters': [15]
         },
    })

