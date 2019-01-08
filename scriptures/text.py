# -*- coding: utf-8 -*-
from scriptures.canons import get_canon
from scriptures.reference import Reference, simplify_refs
import re


class Text:
    def __init__(self, text, language='en', canon='catholic'):
        self.canon = get_canon(canon)(language=language)
        self.language = language
        self.text = text
        self.references = None

        # We set the compiled regex to extract refs in text
        self.__scripture_re = re.compile(
            r'\b(?P<book>%s)\s*\(?\s*'
            r'(?P<chapter>\d{1,3})'
            r'(?:\s*[:,]\s*(?P<verse>\d{1,3}))?'
            r'(?:\w?\s*[-]\s*'
            r'(?P<end_chapter>\d{1,3}(?=\s*[:,]\s*))?'
            r'(?:\s*[:,]\s*)?'
            r'(?P<end_verse>\d{1,3})?'
            r')?'
            r'\s*\)?'
            r'|%s(?P<single_verse>\d{1,3})\s?(?:\s?-\s?(?P<single_verse_end>\d{1,3}))?'
            % (self.canon.book_re_string, self.canon.single_verse_re_string), flags=re.IGNORECASE | re.UNICODE)

        self.__sentence_end_markup = '<sentence_end>'
        self.__sentence_end_re = re.compile(r'\([^\)]*\)|(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s)')

        self.__paragraph_end_markup = '<paragraph_end>'
        self.__paragraph_end_re = re.compile(r'\n+')

    def __repr__(self):
        return self.text

    def extract_refs(self, guess=True, simplify=True):
        """
        Extract a tuple of bible references from text
        :param guess:
        :param simplify:
        :return: [ (<Ref('Book', Chapter, Verse)>, ((char_index_start, char_index_end),) ), ...]
        """
        if guess:
            # We first detect paragraphs and add markups
            marked_text = re.sub(self.__paragraph_end_re, self.__paragraph_end_markup, self.text)

            # Then we detect sentences and add markups
            marked_text = re.sub(self.__sentence_end_re, self.__replace_sen_re, marked_text)

            self.references = list()
            for paragraph in marked_text.split(self.__paragraph_end_markup):
                paragraph_refs = list()
                for sentence in paragraph.split(self.__sentence_end_markup):
                    sentence_refs = list()
                    # If empty string, we skip
                    if not sentence:
                        continue

                    # Else we look for refs in sentence
                    refs = self.find_refs(sentence, valid_only=False)
                    for ref in refs:
                        # If we find partial ref, and we already have a valid ref in sentence, we attribute
                        # same book and chapter
                        if not ref.is_validated and not ref.book and not ref.chapter and len(sentence_refs):
                            ref.book = sentence_refs[0].book
                            ref.chapter = sentence_refs[0].chapter
                            ref.validate(raise_error=False)

                        # If we find partial ref in sentence, but there is no complete ref detected previously
                        # in this sentence, we check first reference of the paragraph ; if it is complete,
                        # we attribute same book and chapter
                        if not ref.is_validated and not ref.book and not ref.chapter and len(paragraph_refs):
                            ref.book = paragraph_refs[0].book
                            ref.chapter = paragraph_refs[0].chapter
                            ref.validate(raise_error=False)

                        # Else, if we attribute the params of the first ref of the page
                        if not ref.is_validated and not ref.book and not ref.chapter and len(self.references):
                            ref.book = self.references[0].book
                            ref.chapter = self.references[0].chapter
                            ref.validate(raise_error=False)

                        if ref.is_validated:
                            sentence_refs.append(ref)

                    paragraph_refs += sentence_refs

                self.references += paragraph_refs

        if not guess:
            self.references = self.find_refs(self.text, valid_only=True)

        if simplify:
            self.references = simplify_refs(self.references)

        return self.references

    def find_refs(self, text, valid_only=False):
        references = list()
        for r in re.finditer(self.__scripture_re, text):
            ref_params = r.groupdict()

            # When we have sth like John 5-6, which is supposed to be chapter 5 to chapter 6,
            # end_chapter is captured by end_verse, so we have to correct it
            if not ref_params.get('verse') and not ref_params.get('end_chapter') and ref_params.get('end_verse'):
                ref_params['end_chapter'] = ref_params.pop('end_verse')

            # If no verse detected, we assign the value of the single verse detected in case we detected sth
            if not ref_params.get('verse') and ref_params.get('single_verse', None):
                ref_params['verse'] = ref_params.get('single_verse')

            if not ref_params.get('end_verse') and ref_params.get('single_verse_end', None):
                ref_params['end_verse'] = ref_params.get('single_verse_end')

            # Then we remove useless extra keys
            ref_params.pop('single_verse', None)
            ref_params.pop('single_verse_end', None)

            ref_params['canon'] = self.canon.name
            ref_params['language'] = self.language

            # We initialize ref object with given values and risk a validation
            ref = Reference(**ref_params)
            ref.validate(raise_error=False)
            if (valid_only and ref.is_validated) or not valid_only:
                references.append(ref)

        return references

    def __replace_sen_re(self, match):
        if not match.groups()[0]:
            return match.group(0)
        return self.__sentence_end_markup
