# bible-ref-parser-py


bible-ref-parser-py is a Python 2 and Python 3 compatible package and regular
expression library for validating, extracting and normalizing biblical
references from texts.

bible-ref-parser-py is built on top of python-scriptures library, implemented by 
[David Davis](http://www.davisd.com/projects/python-scriptures/) (Copyright (c) 2010-2015). His email : [davisd@davisd.com](mailto:davisd@davisd.com).


Typical usage is as follows::
````python
from scriptures.text import Text
string = "Le service est le billet à présenter à l’entrée des noces éternelles. Ce qui reste de la vie au seuil de l’éternité, ce n’est pas ce que nous avons gagné, mais ce que nous avons donné (cf. Mt 6, 19-21 ; 1Co 13, 8)"
text = Text(string, language='fr', canon='catholic')
text.extract_refs(guess=True)
# [<Ref(Matthieu 6:19-21)>, <Ref(I Corinthiens 13:8)>]
````

Range validation is performed automatically and invalid references are not
extracted.
````python
from scriptures.reference import Reference
Reference(book='Rom', chapter=2, verse=30).is_valid()
# False
Reference(book='Rom', chapter=3, verse=23).is_valid()
# True
````

Single verse number references can be guessed, according to what is initially mentioned in the text.
````python
from scriptures.text import Text
string = "Les disciples « sortirent à la rencontre de l’époux » (Mt 25, 1). Puis : « Voici l’époux, sortez à sa rencontre ! » (v. 6)." 
text = Text(string, language='fr', canon='catholic')
text.extract_refs(guess=True)
# [<Ref(Matthieu 25:1)>, <Ref(Matthieu 25:6)>]
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

When a "scripture reference" is returned, it is always an object with five attributes
consisting of:
- book
- chapter
- verse
- end_chapter
- end_verse

```python
from scriptures.reference import Reference
ref = Reference(book='Rom', chapter=2, verse=30)
print(ref.book)
# Romans
print(ref.chapter)
# 2
```


Regular Expressions
-------------------

There are two compiled regular expression patterns exposed by this package.

### book_re


Match a valid abbreviation or book name.

Examples:
````python
from scriptures.canons import get_canon
import re
canon = get_canon(name="catholic")
re.findall(canon.book_re, 'Matt test Ecclesiastes and 2 peter')
# ['Matt', 'Ecclesiastes', '2 peter']    
````


### scripture_re

Match a scripture reference pattern from a valid abbreviation or book name.

Examples:
````python
from scriptures.text import Text
import re
txt = Text("", language="en", canon="catholic")
re.findall(txt.scripture_re, 'Matt 3 & Acts 1:2-3 Rev 2:1-3:2')
# [('Matt', '3', '', '', ''), ('Acts', '1', '2', '', '3'),
# ('Rev', '2', '1', '3', '2')]
````


Canons
================

This library currently provides the following canons:
* catholic - scriptures.canons.catholic.Canon
* protestant - scriptures.canons.protestant.Canon
* deuterocanon - scriptures.canons.deutercanon.Canon
* kjv1611 - scriptures.canons.kjv1611.Canon

Usage
-----

To use the additional texts, simply instantiate the text object and use the api
functions and regular expressions on the new instance.

Example

````python
from scriptures.canons.catholic import Canon
cc = Canon(language='en')
print(cc.books)
# {'gn': {
#                'en': ('Genesis', 'Gen', 'Gen(?:esis)?'),
#                'fr': ('Genèse', 'Gn', 'Gen(?:èse)?'),
#                'chapters':
#                    [31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35,
#                     46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26]
#  },
#  ...}
````


Custom Canons
============

As of v3.0.0, the library makes makes extending the library through custom texts
trivial through additional modules.  Please consider contributing your text
modules to this project by creating canons under scriptures/canons/ and submitting
a pull request.


Creating a New Canon
-------------------

To create a new Canon,

1) Create a class that inherits from scriptures.base.CanonBase
2) Implement the "books" dictionary
3) Instantiate your new canon and use it


Test Suite
==========

Unit tests are provided to verify chapter and verse style normalization, output
formatting, and book names and abbreviations.

To run the test suite, cwd to just outside of the scriptures package and:
```
$ python -m unittest discover
```
