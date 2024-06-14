def main(inn,out):
    for messin in inn.getloop({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES'}):
        orderNumber = messin.get({'BOTSID':'MESSAGES','orderNumber':None})
        dateIssued = messin.get({'BOTSID':'MESSAGES','dateIssued':None})
        deliveryDateStart = messin.get({'BOTSID':'MESSAGES','deliveryDateStart':None})
        deliveryDateEnd = messin.get({'BOTSID':'MESSAGES','deliveryDateEnd':None})
        amazonVendorCode = messin.get({'BOTSID':'MESSAGES','amazonVendorCode':None})
        shipToGLN = messin.get({'BOTSID':'MESSAGES','shipToGLN':None})
        for lin in messin.getloop({'BOTSID':'MESSAGES'},{'BOTSID':'lineItems'}):
            lout = out.putloop({'BOTSID':'LINE'})
            lout.put({'BOTSID':'LINE','orderNumber': orderNumber})
            lout.put({'BOTSID':'LINE','dateIssued': dateIssued})
            lout.put({'BOTSID':'LINE','SKU': ''})
            lout.put({'BOTSID':'LINE','size': ''})
            lout.put({'BOTSID':'LINE','itemNumber': lin.get({'BOTSID':'lineItems','itemNumber':None})})
            lout.put({'BOTSID':'LINE','orderedQuantity': lin.get({'BOTSID':'lineItems','orderedQuantity':None})})
            lout.put({'BOTSID':'LINE','netPrice': lin.get({'BOTSID':'lineItems','netPrice':None})})
            lout.put({'BOTSID':'LINE','deliveryDateStart': deliveryDateStart})
            lout.put({'BOTSID':'LINE','deliveryDateEnd': deliveryDateEnd})
            lout.put({'BOTSID':'LINE','amazonVendorCode': amazonVendorCode})
            lout.put({'BOTSID':'LINE','shipToGLN': shipToGLN})

