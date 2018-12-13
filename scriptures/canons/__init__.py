from importlib import import_module

AVAILABLE_CANONS = [
    'catholic',
    'deuterocanon',
    'kjv1611',
    'protestant',
]
DEFAULT_CANON = 'catholic'


def get_canon(name=DEFAULT_CANON):
    if name not in AVAILABLE_CANONS:
        print("[*] Canon {} does not exist...".format(name))
        print("[*] Available canons are : {}".format(", ".join(AVAILABLE_CANONS)))
        print("[*] Using default canon: {}".format(DEFAULT_CANON))
        name = DEFAULT_CANON

    module = import_module("scriptures.canons.{}".format(name))
    return module.Canon
