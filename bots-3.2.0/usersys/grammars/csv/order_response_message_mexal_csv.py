from bots.botsconfig import *
from mexal_csv import build_syntax, build_structure

syntax = build_syntax()
structure = build_structure()

recorddefs = {
    'LINE': [
        ['BOTSID','M',4,'A'],
        ['orderNumber','M',35,'A'],
        ['SKU','C',8,'A'],
        ['size','C',8,'A'],
        ['itemNumber','C',35,'A'],
        ['orderedQuantity','C',15,'N'],
        ['netPrice','C',15,'R'],
        ['deliveryDateStart','C',35,'A'],
        ['deliveryDateEnd','C',35,'A'],
        ['amazonVendorCode','C',35,'A'],
        ['shipToGLN','C',35,'A'],
    ]
}
