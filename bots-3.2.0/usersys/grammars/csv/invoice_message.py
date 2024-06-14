from bots.botsconfig import *

syntax = {
    'field_sep': ";",
    'charset': 'utf-8',
    'noBOTSID': False,
    'skip_firstline': False,
    'quote_char': '',
    'merge': False,
    'decimaal': ',',
}

structure = [
    {ID:'HEA',MIN:1,MAX:1,LEVEL:[
        {ID:'SUM',MIN:1,MAX:100},
        {ID:'LIN',MIN:1,MAX:100000},
    ]}
]

recorddefs = {
    'HEA': [
        ['BOTSID','M',3,'A'],
        ['taxPointDate','M',35,'A'],
        ['invoiceNumber','M',35,'A'],
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
    'SUM': [
        ['BOTSID','M',3,'A'],
        ['VATRate','M',17,'N'],
        ['taxableAmount','M',18,'R'],
        ['taxAmount','M',18,'R'],
    ],
    'LIN': [
        ['BOTSID','M',3,'A'],
        ['itemNumber','M',35,'A'],
        ['orderNumber','M',35,'A'],
        ['invoicedQuantity','M',15,'N'],
        ['netPrice','M',15,'R'],
        ['totalNetPrice','M',15,'R'],
        ['taxRate','M',17,'N'],
    ]
}
