import bots.transform as transform

def main(inn,out):
    for messin in inn.getloop({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES'}):
        message_run_sequential = transform.unique_runcounter("")
        is_edit_message = True if (messin.get({'BOTSID':'MESSAGES','isEdit':None}) == 'True') else False
        number_of_packages = messin.get({'BOTSID':'MESSAGES','numberOfPackages':None})
        out.put({'BOTSID':'UNH','0062':message_run_sequential,'S009.0065':'DESADV','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN005'})
        #1225:Message function. 5=replace, 9=original
        out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':'351','C002.3055':'9','1004':messin.get({'BOTSID':'MESSAGES','packingListNumber':None}),'1225':'5' if is_edit_message else '9'})
        out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'11','C507.2379':'102','C507.2380':messin.get({'BOTSID':'MESSAGES','despatchDate':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'17','C507.2379':'102','C507.2380':messin.get({'BOTSID':'MESSAGES','estimatedDeliveryDate':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':'102','C507.2380':transform.strftime('%Y%m%d')})
        out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'BM','C506.1154':messin.get({'BOTSID':'MESSAGES','packingListNumber':None})})
        #If the despatch relates to one purchase order, its number can be at the header level and omitted at line item level
        #out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'ON','C506.1154':'PURCHASE ORDER NUMBER'})
        out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'CN','C506.1154':messin.get({'BOTSID':'MESSAGES','shipmentIdentificationNumber':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'CA','C082.3039':messin.get({'BOTSID':'MESSAGES','SCAC':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3055':'9','C082.3039':messin.get({'BOTSID':'MESSAGES','shipToGLN':None}),'3207':messin.get({'BOTSID':'MESSAGES','shipToCountryCode':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3055':'9','C082.3039':messin.get({'BOTSID':'MESSAGES','supplierGLN':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SF','C082.3055':'9','C082.3039':messin.get({'BOTSID':'MESSAGES','shipFromGLN':None}),'3251':messin.get({'BOTSID':'MESSAGES','shipFromPostalCode':None}),'3207':messin.get({'BOTSID':'MESSAGES','shipFromCountryCode':None})})
        #8051:Transport stage qualifier. 20=Main-carriage transport,25=Delivery carrier all transport
        #C220.8067:Mode of transport. 10=sea,20=rail,30=road,40=air
        #C228.8179:Means of transport. 13=Ocean vessel,25=Rail express,31=Truck,41=Aircraft,
        #out.put({'BOTSID':'UNH'},{'BOTSID':'TDT','8051':'20','C220.8067':'30','C228.8179':'31'})
        #A hierarchical division of shipment. level 1 is the whole shipment
        #Levels 2 to n are the package units
        out.put({'BOTSID':'UNH'},{'BOTSID':'CPS','7164':'1'})
        #C202.7065:Package type. 201=ISO EURO pallet,202=UK pallet,PK=Carton
        out.put({'BOTSID':'UNH'},{'BOTSID':'CPS'},{'BOTSID':'PAC','7224':'0','C202.7065':'201'})
        out.put({'BOTSID':'UNH'},{'BOTSID':'CPS'},{'BOTSID':'PAC','7224':number_of_packages,'C202.7065':'PK'})
        item_n = 1
        for package_n, pin in enumerate(messin.getloop({'BOTSID':'MESSAGES'},{'BOTSID':'packages'}), 2):
            pout = out.putloop({'BOTSID':'UNH'},{'BOTSID':'CPS'})
            pout.put({'BOTSID':'CPS','7164':package_n,'7166':'1'})
            #This is a single packing unit, so 7224 is 1
            #C202.7065 Same as above, code for pallet or carton
            pout.put({'BOTSID':'CPS'},{'BOTSID':'PAC','7224':'1','C531.7233':'52','C202.7065':'PK'})
            #C502.6313:Type of measure. LN=Length,WD=Width,HT=Height,AAB=Weight
            #C174.6411:Unit of measure. Non-standard. CMT=cm,KGM=kg
            pout.put({'BOTSID':'CPS'},{'BOTSID':'PAC'},{'BOTSID':'MEA','6311':'PD','C502.6313':'LN','C174.6411':'CMT','C174.6314':pin.get({'BOTSID':'packages','length':None})})
            pout.put({'BOTSID':'CPS'},{'BOTSID':'PAC'},{'BOTSID':'MEA','6311':'PD','C502.6313':'WD','C174.6411':'CMT','C174.6314':pin.get({'BOTSID':'packages','width':None})})
            pout.put({'BOTSID':'CPS'},{'BOTSID':'PAC'},{'BOTSID':'MEA','6311':'PD','C502.6313':'HT','C174.6411':'CMT','C174.6314':pin.get({'BOTSID':'packages','height':None})})
            pout.put({'BOTSID':'CPS'},{'BOTSID':'PAC'},{'BOTSID':'MEA','6311':'PD','C502.6313':'AAB','C174.6411':'KGM','C174.6314':pin.get({'BOTSID':'packages','weight':None})})
            #C524.4079:Optional special handling instructions. BIG=oversized,CRU=fragile,EAT=food,HWC=handle with care
            #lout.put({'BOTSID':'CPS'},{'BOTSID':'PAC'},{'BOTSID':'HAN','C524.4079':'BIG'})
            #4233:Type of package identification. 33E=Serial Shipping Container Code
            pout.put({'BOTSID':'CPS'},{'BOTSID':'PAC'},{'BOTSID':'PCI','4233':'33E'})
            pout.put({'BOTSID':'CPS'},{'BOTSID':'PAC'},{'BOTSID':'PCI'},{'BOTSID':'GIN','7405':'BJ','C208#1.7402#1':pin.get({'BOTSID':'packages','SSCC':None})})
            pout.put({'BOTSID':'CPS'},{'BOTSID':'PAC'},{'BOTSID':'PCI'},{'BOTSID':'RFF','C506.1153':'CN','C506.1154':pin.get({'BOTSID':'packages','trackingNumber':None})})
            for lin in pin.getloop({'BOTSID':'packages'},{'BOTSID':'lineItems'}):
                lout=pout.putloop({'BOTSID':'CPS'},{'BOTSID':'LIN'})
                lout.put({'BOTSID':'LIN','1082':item_n})
                if True:
                    lout.put({'BOTSID':'LIN','C212.7140':lin.get({'BOTSID':'lineItems','itemNumber':None}),'C212.7143':'EN'})
                else:
                    lout.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'5','C212#1.7140':'ALTERNATIVE ITEM NUMBER','C212#1.7143':'BP'})
                lout.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'12','C186.6060':lin.get({'BOTSID':'lineItems','shippedQuantity':None})})
                #If PO number is on header level, it's not required on item level
                lout.put({'BOTSID':'LIN'},{'BOTSID':'RFF','C506.1153':'ON','C506.1154':lin.get({'BOTSID':'lineItems','orderNumber':None})})
                item_n += 1
        out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':message_run_sequential})
