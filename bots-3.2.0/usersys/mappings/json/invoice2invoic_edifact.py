import bots.transform as transform

def main(inn,out):
    for messin in inn.getloop({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES'}):
        message_run_sequential = transform.unique_runcounter("")
        currencyCode = messin.get({'BOTSID':'MESSAGES','currencyISOCode':None})
        out.put({'BOTSID':'UNH','0062':message_run_sequential,'S009.0065':'INVOIC','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN008'})
        #C002.1001:Message type. 380=Commercial invoice, 381=Credit note
        out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':'380','1004':messin.get({'BOTSID':'MESSAGES','invoiceNumber':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':'102','C507.2380':transform.strftime('%Y%m%d')})
        #C507.2005:Date meaning. 35=Delivery date, 131=Tax due date
        #out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'35','C507.2379':'102','C507.2380':'DELDATE'})
        out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'131','C507.2379':'102','C507.2380':messin.get({'BOTSID':'MESSAGES','taxPointDate':None})})
        #Optional supplier's remarks free text
        #out.put({'BOTSID':'UNH'},{'BOTSID':'FTX','4451':'SUR','4453':'1','C108.4440#1':'Free text line, 70 chars','3453':'EN'})
        #RFF containing order number is marked as not used in docs

        #3207:Country code ISO 3166
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3055':'9','C082.3039':messin.get({'BOTSID':'MESSAGES','supplierGLN':None}),'C080.3036#1':messin.get({'BOTSID':'MESSAGES','supplierName1':None}),'C059.3042#1':messin.get({'BOTSID':'MESSAGES','supplierAddress1':None}),'3164':messin.get({'BOTSID':'MESSAGES','supplierCityName':None}),'3251':messin.get({'BOTSID':'MESSAGES','supplierPostcode':None}),'3207':messin.get({'BOTSID':'MESSAGES','supplierCountryCode':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':messin.get({'BOTSID':'MESSAGES','supplierVATNumber':None})})
        #fill conditional info separately so it does nothing if they are empty
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C080.3036#2':messin.get({'BOTSID':'MESSAGES','supplierName2':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C059.3042#2':messin.get({'BOTSID':'MESSAGES','supplierAddress2':None})})
        
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV','C082.3055':'9','C082.3039':messin.get({'BOTSID':'MESSAGES','invoiceeGLN':None}),'C080.3036#1':messin.get({'BOTSID':'MESSAGES','invoiceeName1':None}),'C059.3042#1':messin.get({'BOTSID':'MESSAGES','invoiceeAddress1':None}),'3164':messin.get({'BOTSID':'MESSAGES','invoiceeCityName':None}),'3251':messin.get({'BOTSID':'MESSAGES','invoiceePostcode':None}),'3207':messin.get({'BOTSID':'MESSAGES','invoiceeCountryCode':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':messin.get({'BOTSID':'MESSAGES','invoiceeVATNumber':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV','C080.3036#2':messin.get({'BOTSID':'MESSAGES','invoiceeName2':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV','C059.3042#2':messin.get({'BOTSID':'MESSAGES','invoiceeAddress2':None})})
        #C504#1.6343:Currency meaning. 4=Invoicing currency
        out.put({'BOTSID':'UNH'},{'BOTSID':'CUX','C504#1.6347':'2','C504#1.6345':currencyCode,'C504#1.6343':'4'})
        #Payment terms. Many fields marked as not recommended. They indicate time constraints for payment or discounts.
        out.put({'BOTSID':'UNH'},{'BOTSID':'PAT','4279':'1',})
        #Optional percentage details specifies discount percentage (omitted)
        for n, lin in enumerate(messin.getloop({'BOTSID':'MESSAGES'},{'BOTSID':'lineItems'}), 1):
            lout = out.putloop({'BOTSID':'UNH'},{'BOTSID':'LIN'})
            #1082:Serial item number
            lout.put({'BOTSID':'LIN','1082':str(n)})
            if True:
                #C212.3055:Code list responsible agency, not recommended
                lout.put({'BOTSID':'LIN','C212.7140':lin.get({'BOTSID':'lineItems','itemNumber':None}),'C212.7143':lin.get({'BOTSID':'lineItems','itemNumberType':None})})
            #C186.6063:Meaning of quantity. 47=Invoiced quantity
            #C186.6060:The actual quantity in question
            lout.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'47','C186.6060':lin.get({'BOTSID':'lineItems','invoicedQuantity':None})})
            #C516.5025:Monetary amount type. 203=Line item amount
            #C516.5004:Monetary units
            #C516.6345:Currency ISO code
            #C516.6343:Currency qualifier. 4=Invoicing currency
            lout.put({'BOTSID':'LIN'},{'BOTSID':'MOA','C516.5004':lin.get({'BOTSID':'lineItems','totalNetPrice':None}),'C516.6345':currencyCode,'C516.5025':'203','C516.6343':'4'})
            #C509.5118:Net unit price
            lout.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'AAA','C509.5118':lin.get({'BOTSID':'lineItems','netPrice':None}),'C509.5375':'CT','C509.5387':'NTP'})
            lout.put({'BOTSID':'LIN'},{'BOTSID':'RFF','C506.1153':'ON','C506.1154':lin.get({'BOTSID':'lineItems','orderNumber':None})})
            #Optional original PO date
            #lout.put({'BOTSID':'LIN'},{'BOTSID':'RFF'},{'BOTSID':'DTM','C507.2005':'171','C507.2379':'102','C507.2380':'ORIGINAL PO DATE'})
            #5283:Duty function qualifier. 7=tax
            #C241.5153:Type of duty. VAT=Value added tax
            #5305:Duty category. S=Standard rate
            #C243.5278:The actual rate of duty
            lout.put({'BOTSID':'LIN'},{'BOTSID':'TAX','C243.5278':lin.get({'BOTSID':'lineItems','taxRate':None}),'5283':'7','C241.5153':'VAT','5305':'S'})
            #Copy levy, mandatory if applicable. Idk what it is
            #Followed by nested MOA and TAX
            #lout.put({'BOTSID':'LIN'},{'BOTSID':'ALC','5463':'C','C214.7161':'TX','C214.7160#1':'COPY LEVY'})
        #0081:Type of section separator. S=Summary
        out.put({'BOTSID':'UNH'},{'BOTSID':'UNS','0081':'S'})
        out.put({'BOTSID':'UNH'},{'BOTSID':'CNT','C270.6069':'2','C270.6066':out.getcountoccurrences({'BOTSID':'UNH'},{'BOTSID':'LIN'})})
        #C516.5025:Monetary amount type. 77=Invoice amount
        #C516.5004:Total invoice amount, including tax. (Line item prices were net)
        out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5004':messin.get({'BOTSID':'MESSAGES','invoiceTotal':None}),'C516.5025':'77','C516.6345':currencyCode,'C516.6343':'4'})
        #Total tax rate amount, and monetary amount in MOA
        for summin in messin.getloop({'BOTSID':'MESSAGES'},{'BOTSID':'VATSummaries'}):
            summout = out.putloop({'BOTSID':'UNH'},{'BOTSID':'TAX','BOTSIDnr':'2'})
            summout.put({'BOTSID':'TAX','BOTSIDnr':'2','C243.5278':summin.get({'BOTSID':'VATSummaries','VATRate':None}),'5283':'7','C241.5153':'VAT','5305':'S'})
            #C516.5025:Monetary amount type. 124=Tax amount, 125=Taxable amount
            summout.put({'BOTSID':'TAX','BOTSIDnr':'2'},{'BOTSID':'MOA','C516.5025':'124','C516.5004':summin.get({'BOTSID':'VATSummaries','taxAmount':None}),'C516.6345':currencyCode,'C516.6343':'4'})
            summout.put({'BOTSID':'TAX','BOTSIDnr':'2'},{'BOTSID':'MOA','C516.5025':'125','C516.5004':summin.get({'BOTSID':'VATSummaries','taxableAmount':None}),'C516.6345':currencyCode,'C516.6343':'4'})
        out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':message_run_sequential})
