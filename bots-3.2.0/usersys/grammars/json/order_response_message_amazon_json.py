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
            ['deliveryDateStart','C',35,'A'],
            ['deliveryDateEnd','C',35,'A'],
            ['amazonVendorCode','C',35,'A'],
            ['shipToGLN','C',35,'A'],
        ],
        'lineItems':[
            ['BOTSID','M',9,'A'],
            ['itemNumber','M',35,'A'],
            ['itemNumberType','C',3,'A'],
            ['SKU','C',35,'A'],
            ['size','C',35,'A'],
            ['orderedQuantity','M',15,'N'],
            ['netPrice','M',15,'R'],
        ],
    }
)
