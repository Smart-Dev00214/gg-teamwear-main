from bots.botsconfig import *
from amazon_json import build_structure, build_recorddefs

structure = build_structure([
    {ID:'packages',MIN:1,MAX:10000,LEVEL:[
        {ID:'lineItems',MIN:1,MAX:10000}
    ]}
])

recorddefs = build_recorddefs(
    {
        'MESSAGES':[
            ['BOTSID','M',8,'A'],
            ['packingListNumber','M',35,'A'],
            ['shipmentIdentificationNumber','M',35,'A'],
            ['despatchDate','M',8,'A'],
            ['estimatedDeliveryDate','M',8,'A'],
            ['shipToGLN','M',35,'A'],
            ['shipToCountryCode','M',2,'A'],
            ['supplierGLN','M',35,'A'],
            ['shipFromGLN','M',35,'A'],
            ['shipFromCountryCode','M',2,'A'],
            ['shipFromPostalCode','M',35,'A'],
            ['SCAC','M',35,'A'],
            ['numberOfPackages','M',5,'N'],
            ['isEdit','M',5,'A'],
        ],
        'packages':[
            ['BOTSID','M',8,'A'],
            ['length','M',5,'R'],
            ['width','M',5,'R'],
            ['height','M',5,'R'],
            ['weight','M',5,'R'],
            ['SSCC','M',35,'A'],
            ['trackingNumber','M',35,'A'],
        ],
        'lineItems':[
            ['BOTSID','M',9,'A'],
            ['itemNumber','M',35,'A'],
            ['shippedQuantity','M',10,'N'],
            ['orderNumber','M',35,'A'],
        ]
    }
)
