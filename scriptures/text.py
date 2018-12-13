from scriptures.canons import get_canon
from scriptures.reference import Reference
import re


class Text:
    def __init__(self, text, language='en', canon='catholic'):
        self.canon = get_canon(canon)(language=language)
        self.language = language
        self.text = text

    def extract_refs(self, ):
        """
        Extract a tuple of bible references from text
        """
        references = list()
        for r in re.finditer(self.canon.scripture_re, self.text):
            ref = Reference(*r.groups(), canon=self.canon)
            references.append(ref.normalize())

        return references
