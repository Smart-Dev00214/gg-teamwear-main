from bots.botsconfig import *
from amazon_json import build_structure, build_recorddefs

structure = build_structure([
    {ID:'lineItems',MIN:0,MAX:200000}
])

recorddefs = build_recorddefs(
    {
        'MESSAGES':[
            ['BOTSID','M',8,'A'],
            ['orderNumber','M',35,'A'],
            ['supplierGLN','M',35,'A'],
            ['shipToGLN','M',35,'A'],
            ['shipToCountryCode','M',3,'A'],
            ['currencyISOCode','M',3,'A'],
            ['containsChanges','M',5,'A'],
        ],
        'lineItems':[
            ['BOTSID','M',9,'A'],
            ['itemNumber','M',35,'A'],
            ['itemNumberType','M',3,'A'],
            ['quantityDispatching','C',15,'N'],
            ['quantityBackorder','C',15,'N'],
            ['quantityHardReject','C',15,'N'],
            ['quantitySoftReject','C',15,'N'],
            ['netPrice','M',15,'R'],
            ['vatRate','C',15,'R'],
            ['containsChanges','M',5,'A'],
        ],
    }
)
