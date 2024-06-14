def main(inn,out):
    firstloop = True
    is_message_empty = True
    for lin in inn.getloop({'BOTSID':'LINE'}):
        if firstloop:
            out.put({'BOTSID': 'ROOT'},{'BOTSID':'MESSAGES','orderNumber': lin.get({'BOTSID':'LINE', 'orderNumber':None})})
            
            delivery_date_start = lin.get({'BOTSID':'LINE', 'deliveryDateStart':None})
            out.put({'BOTSID': 'ROOT'},{'BOTSID':'MESSAGES','deliveryDateStart': delivery_date_start})
            
            delivery_date_end = lin.get({'BOTSID':'LINE', 'deliveryDateEnd':None})
            out.put({'BOTSID': 'ROOT'},{'BOTSID':'MESSAGES','deliveryDateEnd': delivery_date_end})
            
            amazon_vendor_code = lin.get({'BOTSID':'LINE', 'amazonVendorCode':None})
            out.put({'BOTSID': 'ROOT'},{'BOTSID':'MESSAGES','amazonVendorCode': amazon_vendor_code})
            
            ship_to_gln = lin.get({'BOTSID':'LINE', 'shipToGLN':None})
            out.put({'BOTSID': 'ROOT'},{'BOTSID':'MESSAGES','shipToGLN': ship_to_gln})
            
            if any([delivery_date_start, delivery_date_end, amazon_vendor_code, ship_to_gln]):
                is_message_empty = False
            firstloop = False
        if  not is_message_empty:
            lout = out.putloop({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES'},{'BOTSID':'lineItems'})
            lout.put({'BOTSID':'lineItems', 'SKU': lin.get({'BOTSID':'LINE', 'SKU':None})})
            lout.put({'BOTSID':'lineItems', 'size': lin.get({'BOTSID':'LINE', 'size':None})})
            lout.put({'BOTSID':'lineItems', 'itemNumber': lin.get({'BOTSID':'LINE', 'itemNumber':None})})
            lout.put({'BOTSID':'lineItems', 'orderedQuantity': lin.get({'BOTSID':'LINE', 'orderedQuantity':None})})
            lout.put({'BOTSID':'lineItems', 'netPrice': lin.get({'BOTSID':'LINE', 'netPrice':None})})
