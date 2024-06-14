from bots.botsconfig import *
from mexal_csv import build_syntax, build_structure

syntax = build_syntax()
structure = build_structure()

recorddefs = {
    'LINE': [
        ['BOTSID','M',4,'A'],
        ['orderNumber','M',35,'A'],
        ['dateIssued','M',35,'A'],
        ['SKU','C',8,'A'],
        ['size','C',8,'A'],
        ['itemNumber','M',35,'A'],
        ['orderedQuantity','M',15,'N'],
        ['netPrice','M',15,'R'],
        ['deliveryDateStart','M',35,'A'],
        ['deliveryDateEnd','M',35,'A'],
        ['amazonVendorCode','M',35,'A'],
        ['shipToGLN','M',35,'A'],
    ]
}
