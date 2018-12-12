from .texts.catholic import CatholicCanon

# create an instance of the Protestant Canon to use as the default
cc = CatholicCanon()

book_re = cc.book_re
scripture_re = cc.scripture_re

