# Bible Ref Parser Py


bible-ref-parser-py is a Python 2 and Python 3 compatible package and regular
expression library for validating, extracting and normalizing biblical
scripture references from blocks of text.

For more information, see http://www.davisd.com/projects/python-scriptures/

Typical usage is as follows::
````python
#!/usr/bin/env python
import scriptures
scriptures.extract('This is a test Rom 3:23-28 and 1 JOHn 2')
# [('Romans', 3, 23, 3, 28), ('I John', 2, 1, 2, 29)]
````

Range validation is performed automatically and invalid references are not
extracted.
````python
import scriptures
scriptures.extract('Romans 3:23 is real, but Romans 2:30 is invalid.')
# [('Romans', 3, 23, 3, 23)]
````

Multi-Chapter references work:
````python
import scriptures
scriptures.extract('You can specify a range of chapters like Rev 2-3')
# [('Revelation of Jesus Christ', 2, 1, 3, 22)]
````
    
References with single chapter books do not require the chapter be specified.
````python
import scriptures
scriptures.extract('You can specify a single verse such as Jude 4')
# [('Jude', 1, 4, 1, 4)]
scriptures.extract('Or specify multiple verses with jude 2-5...')
# [('Jude', 1, 2, 1, 5)]
````


Installation
============

A setup script (setup.py) is provided.  To install, simply run the script with
the install command:
````shell
$ pip install git+https://github.com/beatitud/bible-ref-parser-py.git@master
````

Or just put the scriptures package somewhere on the Python path.


API
===

Return Values
-------------

When a "scripture reference" is returned, it is always a five value tuple
consisting of:

('Book name', start chapter, start verse, end chapter, end verse)


Functions
---------

There are four public functions exposed by this package.

### extract

Extract a list of tupled scripture references from a block of text.

Arguments:

    text -- the block of text containing potential scripture references

Example:
````python
import scriptures
scriptures.extract('This is a test Rom 3:23-28 and 1 JOHn 2')
# [('Romans', 3, 23, 3, 28), ('I John', 2, 1, 2, 29)]
````


### reference_to_string

Get a display friendly string from a scripture reference.

Arguments:

    bookname -- the full or abbreviated book name

    chapter -- the starting chapter

Optional Arguments:

    verse -- the starting verse

    end_chapter -- the ending chapter

    end_verse -- the ending verse

Examples:
````python
import scriptures
scriptures.reference_to_string('acts', 1)
# 'Acts 1'
scriptures.reference_to_string('John', 3, 16)
# 'John 3:16'
scriptures.reference_to_string('Rom', 3, 23, 3, 28)
# 'Romans 3:23-28'
scriptures.reference_to_string('ecc', 1, 2, 2)
# 'Ecclesiastes 1:2-2:26'
scriptures.reference_to_string('john', 1, 1, 2, 25)
# 'John 1-2'
````

Single Chapter Book Examples:
````python
import scriptures
scriptures.reference_to_string('jude', 1, 4)
# 'Jude 4'
scriptures.reference_to_string('2john', 1, 4, 1, 7)
# 'II John 4-7'
````


### normalize_reference

Get a complete five value tuple scripture reference with full book name from
partial data.

Arguments:

    bookname -- the full or abbreviated book name

    chapter -- the starting chapter

Optional Arguments:

    verse -- the starting verse

    end_chapter -- the ending chapter

    end_verse -- the ending verse

Examples:
````python
import scriptures
scriptures.normalize_reference('acts', 1)
# ('Acts', 1, 1, 1, 26)
scriptures.normalize_reference('John', 3, 16)
# ('John', 3, 16, 3, 16)
scriptures.normalize_reference('Rom', 3, 23, 3, 28)
# ('Romans', 3, 23, 3, 28)
scriptures.normalize_reference('ecc', 1, 2, 2)
# ('Ecclesiastes', 1, 2, 2, 26)
````


### is_valid_reference

Check to see if a scripture reference is valid.

Arguments:

    bookname -- the full or abbreviated book name

    chapter -- the starting chapter

Optional Arguments:

    verse -- the starting verse

    end_chapter -- the ending chapter

    end_verse -- the ending verse

Examples:
````python
import scriptures
scriptures.is_valid_reference('John', 3, 16)
# True
scriptures.is_valid_reference('ecc', 1, 2, 2)
# True
scriptures.is_valid_reference('Romans', 2, 30)
# False
scriptures.is_valid_reference('Romans', 2, 20, 2, 29)
# True
````


Regular Expressions
-------------------

There are two compiled regular expression patterns exposed by this package.

### book_re


Match a valid abbreviation or book name.

Examples:
````python
import scriptures
import re
re.findall(scriptures.book_re, 'Matt test Ecclesiastes and 2 peter')
# ['Matt', 'Ecclesiastes', '2 peter']    
````


### scripture_re

Match a scripture reference pattern from a valid abbreviation or book name.

Examples:
````python
import scriptures
import re
re.findall(scriptures.scripture_re, 'Matt 3 & Acts 1:2-3 Rev 2:1-3:2')
# [('Matt', '3', '', '', ''), ('Acts', '1', '2', '', '3'),
# ('Rev', '2', '1', '3', '2')]
````


Unicode
=======

This library is unicode compatible and recognizes the \u2013 en dash and \u2014
em dash.


Additional Texts
================

This library currently provides the following texts:

* protestant - scriptures.texts.protestant.ProtestantCanon
* deuterocanon - scriptures.texts.deutercanon.Deuterocanon
* kjv1611 - scriptures.texts.kjv1611.KingJames1611

Usage
-----

To use the additional texts, simply instantiate the text object and use the api
functions and regular expressions on the new instance.

Example

````python
from scriptures.texts.kjv1611 import KingJames1611
myKJV1611 = KingJames1611()
myKJV1611.extract('the protestant books are implemented- Matthew 1:1-5')
# [(u'Matthew', 1, 1, 1, 5)]
myKJV1611.extract('and Deuterocanon (apocrypha)- wisdom of solomon 1:1')
# [(u'The Wisdom of Solomon', 1, 1, 1, 1)]
myKJV1611.extract('and I Esd 1:1, II Esd 1:1, Prayer of Manasseh 1:1')
# [(u'I Esdras', 1, 1, 1, 1), (u'II Esdras', 1, 1, 1, 1), (u'Prayer of Manasseh', 1, 1, 1, 1)]
````


Custom Texts
============

As of v3.0.0, the library makes makes extending the library through custom texts
trivial through additional modules.  Please consider contributing your text
modules to this project by creating texts under scriptures/texts/ and submitting
a pull request.


Creating a New Text
-------------------

To create a new Text,

1) Create a class that inherits from scriptures.base.Text
2) Implement the "books" dictionary
3) Instantiate your new text and use it

The four api functions will be available from your instance:

* extract
* reference_to_string
* normalize_reference
* is_valid_reference

The two regular expressions are also available:

* book_re
* scripture_re


Example

````python
from scriptures.texts.base import Text
class MyText(Text):
    books = {
        'test1': ('Test Book 1', 'TBook1', 'test(?:\s)?1', [5, 4, 3, 4, 5]),
        'test2': ('Test Book 2', 'TBook2', 'test(?:\s)?2', [5, 4, 3, 4, 5])
    }
    
mytext = MyText()
mytext.extract('Ok, testing- test1 1:3-5 and test2 2:4')
# [('Test Book 1', 1, 3, 1, 5), ('Test Book 2', 2, 4, 2, 4)]
````


Creating a New Text Using Another As a Starting Point
-----------------------------------------------------

If you would like to use an existing set of books as a starting point, simply
update your books dictionary using the books from the Text class (or classes)
that you'd like to use as a starting point.

For an example of this, see the "KingJames1611" text class in 
scriptures/text/kjv1611.py

The KingJames1611 Text class uses the ProtestantCanon and Deuterocanon books as
a starting point and adds I Esdras, II Esdras, and the Prayer of Manasseh.

Test Suite
==========

Unit tests are provided to verify chapter and verse style normalization, output
formatting, and book names and abbreviations.

To run the test suite, cwd to just outside of the scriptures package and:
```
$ python -m unittest discover
```


Author
======

David Davis <davisd@davisd.com>
http://www.davisd.com

