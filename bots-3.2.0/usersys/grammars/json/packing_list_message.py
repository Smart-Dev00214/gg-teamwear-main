from bots.botsconfig import *
from amazon_json import build_structure, build_recorddefs

syntax = {
    'charset': 'utf-8',
}

structure = build_structure([
    {ID:'packages',MIN:1,MAX:10000,LEVEL:[
        {ID:'lineItems', MIN:0,MAX:10000},
    ]},
])

recorddefs = build_recorddefs(
    {
        'MESSAGES':[
            ['BOTSID','M',8,'A'],
            ['documentNumber','M',35,'A'],
            ['shipToGLN','M',35,'A'],
            ['shipToName','M',70,'A'],
            ['shipToAddressLine1','M',70,'A'],
            ['shipToAddressLine2','C',70,'A'],
            ['shipToCity','M',70,'A'],
            ['shipToCountryCode','M',2,'A'],
            ['shipToPostalCode','M',35,'A'],
        ],
        'packages':[
            ['BOTSID','M',8,'A'],
            ['packageNumber','M',35,'A'],
            ['weight','M',10,'R'],
            ['width','M',10,'R'],
            ['length','M',10,'R'],
            ['height','M',10,'R'],
            ['SSCC','M',35,'A'],
        ],
        'lineItems':[
            ['BOTSID','M',9,'A'],
            ['orderNumber','M',35,'A'],
            ['itemNumber','M',35,'A'],
            ['shippedQuantity','M',15,'N'],
        ]
    }
)
