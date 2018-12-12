from .bible_re import cc
from .texts import InvalidReferenceException

# The functions below are shortcut-functions to the ProtestantCanon text
# The same functions could be verbosely accessed with:
#
#    >>> from scriptures.texts.protestant import ProtestantCanon
#    >>> pc=ProtestantCanon()
#
#    The instance variable "pc" has the functions: get_book, extract,
#    is_valid_reference, reference_to_string, and normalize_reference
#
# For instructions on using a different Text, see the documentation

canon = cc


def get_book(name):
    """
    Get a book from its name or None if not found
    """
    return canon.get_book(name)


def extract(text):
    """
    Extract a list of tupled scripture references from a block of text
    """
    return canon.extract(text)


def is_valid_reference(bookname, chapter, verse=None,
                                 end_chapter=None, end_verse=None):
    """
    Check to see if a scripture reference is valid
    """
    return canon.is_valid_reference(bookname, chapter, verse, end_chapter,
            end_verse)


def reference_to_string(bookname, chapter, verse=None,
                        end_chapter=None, end_verse=None):
    """
    Get a display friendly string from a scripture reference
    """
    return canon.reference_to_string(bookname, chapter, verse,
            end_chapter, end_verse)


def normalize_reference(bookname, chapter, verse=None,
                                  end_chapter=None, end_verse=None):
    """
    Get a complete five value tuple scripture reference with full book name
    from partial data
    """
    return canon.normalize_reference(bookname, chapter, verse, end_chapter,
            end_verse)
