from bots.botsconfig import *

syntax = {
    'field_sep': ";",
    'charset': 'unoc',
    'noBOTSID': False,
    'skip_firstline': False,
    'quote_char': '',
    'merge': False,
    'decimaal': ',',
}

structure = [
    {ID:'SHP',MIN:1,MAX:1,LEVEL:[
        {ID:'ADR',MIN:1,MAX:1},
        {ID:'PAC',MIN:1,MAX:10000,LEVEL:[
            {ID:'LIN',MIN:1,MAX:10000},
        ]},
    ]}
]

recorddefs = {
    'SHP': [
        ['BOTSID','M',3,'A'],
        ['documentNumber','M',35,'A'],
    ],
    'ADR': [
        ['BOTSID','M',3,'A'],
        ['shipToGLN','M',35,'A'],
        ['shipToName','M',70,'A'],
        ['shipToAddressLine1','M',70,'A'],
        ['shipToAddressLine2','C',70,'A'],
        ['shipToCity','M',70,'A'],
        ['shipToCountryCode','M',2,'A'],
        ['shipToPostalCode','M',35,'A'],
    ],
    'PAC': [
        ['BOTSID','M',3,'A'],
        ['packageNumber','M',35,'A'],
        ['weight','M',10,'R'],
        ['width','M',10,'R'],
        ['length','M',10,'R'],
        ['height','M',10,'R'],
        ['SSCC','M',35,'A'],
    ],
    'LIN': [
        ['BOTSID','M',3,'A'],
        ['orderNumber','M',35,'A'],
        ['itemNumber','M',35,'A'],
        ['shippedQuantity','M',15,'N'],
    ],
}
