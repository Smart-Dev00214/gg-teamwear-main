import bots.transform as transform

def main(inn,out):
    for messin in inn.getloop({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES'}):
        ordrsp_message_sequential = transform.unique("ordrsp_id")
        message_run_sequential = transform.unique_runcounter("")
        order_contains_changes = True if (messin.get({'BOTSID':'MESSAGES','containsChanges':None}) == 'True') else False
        #0062:Consecutive message reference if more than 1 message in interchange
        out.put({'BOTSID':'UNH','0062':message_run_sequential,'S009.0065':'ORDRSP','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN005'})
        #1004:Message reference number, may need to be unique between exchanges?
        #1225:Message function. 4=amendment, 29=order accept
        out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':'231','1004':'{:0>8}'.format(ordrsp_message_sequential),'1225': '4' if order_contains_changes else '29'})
        #Issue date YYYYMMDD
        out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':'102','C507.2380':transform.strftime('%Y%m%d')})
        #PO reference number
        out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'ON','C506.1154':messin.get({'BOTSID':'MESSAGES','orderNumber':None})})
        #C082.3039:Supplier GLN
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3055':'9','C082.3039':messin.get({'BOTSID':'MESSAGES','supplierGLN':None})})
        #C082.3039:Deliveree GLN
        #3207:Country code ISO 3166-1 alpha-2
        #out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3055':'9','C082.3039':messin.get({'BOTSID':'MESSAGES','shipToGLN':None}),'3207':messin.get({'BOTSID':'MESSAGES','shipToCountryCode':None})})
        #C504#1.6345:Currency ISO code
        out.put({'BOTSID':'UNH'},{'BOTSID':'CUX','C504#1.6347':'2','C504#1.6345':messin.get({'BOTSID':'MESSAGES','currencyISOCode':None}),'C504#1.6343':'9'})
        #loop over order items from input file
        for n, lin in enumerate(messin.getloop({'BOTSID':'MESSAGES'},{'BOTSID':'lineItems'}), 1):
            lout = out.putloop({'BOTSID':'UNH'},{'BOTSID':'LIN'})
            line_contains_changes = True if (lin.get({'BOTSID':'lineItems', 'containsChanges':None}) == 'True') else False
            #1082:Serial item number
            lout.put({'BOTSID':'LIN','1082':str(n)})
            #1229:Action to be taken. 3=changed, 5=accepted, 10=not found
            lout.put({'BOTSID':'LIN','1229': '3' if line_contains_changes else '5'})
            #Item identification can be missing from here if the order was made with
            #an ID other than EAN or UPC. In that case a PIA is mandatory after LIN
            if True:
                #C212.7143:Type of item ID. EN=EAN, UP=UPC, SRV=GTIN
                lout.put({'BOTSID':'LIN','C212.7143':lin.get({'BOTSID':'lineItems', 'itemNumberType':None}),'C212.7140':lin.get({'BOTSID':'lineItems', 'itemNumber':None})})
            else:
                #4347:Function of the product code. 1=additional id, 5=main id(when LIN id missing)
                #C212#1.7143:Type of product code. BP=Buyer-assigned id, IB=ISBN, SA=Supplier-assigned id
                lout.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'5','C212#1.7143':'SA','C212#1.7140':'ADDCODE'})
            #C186.6063:Code giving meaning to a quantity. 12=Dispatching, 83=Backorder, 182=Hard reject, 185=Soft reject, 192=Free goods
            #C186.6060:The actual quantity in question
            lout.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'12','C186.6060':lin.get({'BOTSID':'lineItems','quantityDispatching':None})})
            lout.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'83','C186.6060':lin.get({'BOTSID':'lineItems','quantityBackorder':None})})
            lout.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'182','C186.6060':lin.get({'BOTSID':'lineItems','quantityHardReject':None})})
            lout.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'185','C186.6060':lin.get({'BOTSID':'lineItems','quantitySoftReject':None})})
            #C507.2005:Type of date. 11=Despatch date, 67=Delivery date
            # lout.put({'BOTSID':'LIN'},{'BOTSID':'DTM','C507.2005':'67','C507.2379':'102','C507.2380':DATE})
            #C509.5118:Price
            lout.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'AAA','C509.5375':'CT','C509.5387':'NTP','C509.5118':lin.get({'BOTSID':'lineItems','netPrice':None})})
            #C243.5278:VAT rate
            lout.put({'BOTSID':'LIN'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':lin.get({'BOTSID':'lineItems','vatRate':None})})
        #0081:Next section identifier. S=Summary
        out.put({'BOTSID':'UNH'},{'BOTSID':'UNS','0081':'S'})
        #C270.6069:Type of control. 2=Number of line items
        out.put({'BOTSID':'UNH'},{'BOTSID':'CNT','C270.6069':'2','C270.6066':out.getcountoccurrences({'BOTSID':'UNH'},{'BOTSID':'LIN'})})
        #0074:Number of segments in message
        #0062:Unique message reference
        out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':message_run_sequential})
