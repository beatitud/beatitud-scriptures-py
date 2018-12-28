from setuptools import find_packages, setup

setup(
    name='bible-ref-py',
    version='4.0.0',
    author='Antoine Rose',
    author_email='antoine_rose@hotmail.fr',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=open("./requirements.pip").readlines(),
    license='MIT',
    description='bible-ref-py is a python library built on top of python-scriptures library, '
                'implemented by David Davis <davisd@davisd.com> (Copyright (c) 2010-2015). It is a Python '
                'package and regular expression library for validating, extracting, and normalizing '
                'biblical references from text.',
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/beatitud/bible-ref-py/",
    keywords=['bible', 'ref', 'parser', 'catholic', 'protestant'],
)
