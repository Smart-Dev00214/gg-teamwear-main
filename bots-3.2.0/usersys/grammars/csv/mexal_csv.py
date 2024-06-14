from bots.botsconfig import *

def build_syntax():
    return {
        'field_sep': ";",
        'charset': 'utf-8',
        'noBOTSID': True,
        'skip_firstline': False,
        'quote_char': '',
        'merge': False,
        'decimaal': ',',
    }

def build_structure():
    return [
        {ID:'LINE',MIN:1,MAX:9999},
    ]
