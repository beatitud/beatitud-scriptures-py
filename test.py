if __name__ == '__main__':
    import re
    reg = '\s[v]{1,2}[.]?\s{0,2}(?P<single_verse>\d{1,3})\s?(?:-\s?(?P<single_verse_end>\d{1,3}))?'
    text = '(cf. vv. 2- 4)'
    print(re.findall(re.compile(reg, re.IGNORECASE), text))
    from scriptures.text import Text
    t = Text(text, language='fr')
    print(t.extract_refs(guess=True))
