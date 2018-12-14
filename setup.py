from distutils.core import setup

setup(
    name='bible-ref-parser-py',
    version='1.0.0',
    author='Antoine Rose',
    author_email='antoine_rose@hotmail.fr',
    packages=['scriptures', 'scriptures/canons'],
    data_files=[('.', ['LICENSE'])],
    license='LICENSE',
    description='bible-ref-parser-py is a python library built on top of python-scriptures library, '
                'implemented by David Davis <davisd@davisd.com> (Copyright (c) 2010-2015). It is a Python '
                'package and regular expression library for validating, extracting, and normalizing '
                'biblical references from text.',
    long_description=open('README.md').read(),
)
