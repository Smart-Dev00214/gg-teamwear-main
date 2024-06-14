from bots.botsconfig import *
from amazon_json import build_structure, build_recorddefs

structure = build_structure([
    {ID:'lineItems',MIN:1,MAX:200000}
])

recorddefs = build_recorddefs(
    {
        'MESSAGES':[
            ['BOTSID','M',8,'A'],
            ['orderNumber','M',35,'A'],
            ['dateIssued','M',35,'A'],
            ['deliveryDateStart','M',35,'A'],
            ['deliveryDateEnd','M',35,'A'],
            ['amazonVendorCode','M',35,'A'],
            ['shipToGLN','M',35,'A'],
        ],
        'lineItems':[
            ['BOTSID','M',9,'A'],
            ['itemNumber','M',35,'A'],
            ['itemNumberType','C',3,'A'],
            ['orderedQuantity','M',15,'N'],
            ['netPrice','M',15,'R'],
        ],
    }
)
