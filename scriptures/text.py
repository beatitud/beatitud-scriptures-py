from scriptures.canons import get_canon
from scriptures.reference import Reference
import re


class Text:
    def __init__(self, text, language='en', canon='catholic'):
        self.canon = get_canon(canon)(language=language)
        self.language = language
        self.text = text
        self.references = None

        # We set the compiled regex to extract refs in text
        self.scripture_re = re.compile(
            r'\b(?P<book>%s)\s*'
            r'(?P<chapter>\d{1,3})?'
            r'(?:\s*[:,]\s*(?P<verse>\d{1,3}))?'
            r'(?:\s*[-]\s*'
            r'(?P<end_chapter>\d{1,3}(?=\s*:\s*))?'
            r'(?:\s*:\s*)?'
            r'(?P<end_verse>\d{1,3})?'
            r')?'
            r'|\b%s(?P<single_verse>\d{1,3})?\s*'
            % (self.canon.book_re_string, self.canon.single_verse_re_string), re.IGNORECASE | re.UNICODE)

    def extract_refs(self, ):
        """
        Extract a tuple of bible references from text
        """
        self.references = list()
        for r in re.finditer(self.scripture_re, self.text):
            ref_params = r.groupdict()
            if not ref_params.get('verse'):
                ref_params['verse'] = ref_params.pop('single_verse')
            ref_params.pop('single_verse', None)
            ref_params['canon'] = self.canon
            ref = Reference(**ref_params)
            ref.validate(raise_error=False)
            self.references.append(ref)

        return self.references

    def guess_partial_refs(self):
        for ref in self.references:
            pass
