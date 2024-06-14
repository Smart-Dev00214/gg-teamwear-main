from bots.botsconfig import *
from amazon_json import build_structure, build_recorddefs

structure = build_structure([
    {ID:'lineItems', MIN:0,MAX:200000},
    {ID:'VATSummaries',MIN:0,MAX:200000}
])

recorddefs = build_recorddefs(
    {
        'MESSAGES':[
            ['BOTSID','M',8,'A'],
            ['invoiceNumber','M',35,'A'],
            ['taxPointDate','M',35,'A'],
            ['invoiceeGLN','M',35,'A'],
            ['invoiceeName1','M',35,'A'],
            ['invoiceeName2','C',35,'A'],
            ['invoiceeAddress1','M',35,'A'],
            ['invoiceeAddress2','C',35,'A'],
            ['invoiceeCityName','M',35,'A'],
            ['invoiceePostcode','M',9,'A'],
            ['invoiceeCountryCode','M',2,'A'],
            ['invoiceeVATNumber','M',35,'A'],
            ['invoiceTotal','M',18,'R'],
        ],
        'lineItems':[
            ['BOTSID','M',9,'A'],
            ['itemNumber','M',35,'A'],
            ['invoicedQuantity','M',15,'N'],
            ['totalNetPrice','M',18,'R'],
            ['netPrice','M',15,'R'],
            ['orderNumber','M',35,'A'],
            ['taxRate','M',17,'N'],
        ],
        'VATSummaries':[
            ['BOTSID','M',12,'A'],
            ['VATRate','M',17,'N'],
            ['taxAmount','M',18,'R'],
            ['taxableAmount','M',18,'R'],
        ]
    }
)
