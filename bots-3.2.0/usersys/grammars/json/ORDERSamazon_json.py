from bots.botsconfig import *
from amazon_json import build_structure, build_recorddefs

structure = build_structure([
    {ID:'lineItems',MIN:1,MAX:200000}
])

recorddefs = build_recorddefs(
    {
        'MESSAGES':[
            ['BOTSID','M',8,'A'],
            ['marketplace','M',2,'A'],
            ['orderNumber','M',35,'A'],
            ['dateIssued','M',35,'A'],
            ['deliveryDateStart','M',35,'A'],
            ['deliveryDateEnd','M',35,'A'],
            ['firstOrderStatus','C',35,'A'],
            ['promotionDealNumber','C',35,'A'],
            ['amazonVendorCode','M',35,'A'],
            ['buyerGLN','M',35,'A'],
            ['supplierGLN','M',35,'A'],
            ['shipToGLN','M',35,'A'],
            ['shipToCountryCode','M',3,'A'],
            ['invoiceeGLN','M',35,'A'],
            ['invoiceeName1','M',35,'A'],
            ['invoiceeName2','C',35,'A'],
            ['invoiceeAddress1','M',35,'A'],
            ['invoiceeAddress2','C',35,'A'],
            ['invoiceeCity','M',35,'A'],
            ['invoiceeState','C',9,'A'],
            ['invoiceePostcode','M',9,'A'],
            ['invoiceeCountry','M',3,'A'],
            ['VATNumber','C',35,'A'],
            ['currencyISOCode','M',3,'A'],
            ['totalLineItemsControl','M',18,'N'],
        ],
        'lineItems':[
            ['BOTSID','M',9,'A'],
            ['lineItemNumber','M',6,'N'],
            ['itemNumber','C',35,'A'],
            ['itemNumberType','C',3,'A'],
            ['additionalProductId','C',35,'A'],
            ['additionalProductIdType','C',3,'A'],
            ['orderedQuantity','M',15,'N'],
            ['netPrice','M',15,'R'],
        ],
    }
)
