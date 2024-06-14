def main(inn,out):
    for hin in inn.getloop({'BOTSID':'HEA'}):
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceNumber':hin.get({'BOTSID':'HEA','invoiceNumber':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','taxPointDate':hin.get({'BOTSID':'HEA','taxPointDate':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceeGLN':hin.get({'BOTSID':'HEA','invoiceeGLN':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceeName1':hin.get({'BOTSID':'HEA','invoiceeName1':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceeName2':hin.get({'BOTSID':'HEA','invoiceeName2':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceeAddress1':hin.get({'BOTSID':'HEA','invoiceeAddress1':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceeAddress2':hin.get({'BOTSID':'HEA','invoiceeAddress2':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceeCityName':hin.get({'BOTSID':'HEA','invoiceeCityName':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceePostcode':hin.get({'BOTSID':'HEA','invoiceePostcode':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceeCountryCode':hin.get({'BOTSID':'HEA','invoiceeCountryCode':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceeVATNumber':hin.get({'BOTSID':'HEA','invoiceeVATNumber':None})})
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','invoiceTotal':hin.get({'BOTSID':'HEA','invoiceTotal':None})})

        for sin in hin.getloop({'BOTSID':'HEA'},{'BOTSID':'SUM'}):
            sout = out.putloop({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES'},{'BOTSID':'VATSummaries'})
            sout.put({'BOTSID':'VATSummaries','VATRate':sin.get({'BOTSID':'SUM','VATRate':None})})
            sout.put({'BOTSID':'VATSummaries','taxAmount':sin.get({'BOTSID':'SUM','taxAmount':None})})
            sout.put({'BOTSID':'VATSummaries','taxableAmount':sin.get({'BOTSID':'SUM','taxableAmount':None})})

        for lin in hin.getloop({'BOTSID':'HEA'},{'BOTSID':'LIN'}):
            lout = out.putloop({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES'},{'BOTSID':'lineItems'})
            lout.put({'BOTSID':'lineItems','itemNumber':lin.get({'BOTSID':'LIN','itemNumber':None})})
            lout.put({'BOTSID':'lineItems','invoicedQuantity':lin.get({'BOTSID':'LIN','invoicedQuantity':None})})
            lout.put({'BOTSID':'lineItems','totalNetPrice':lin.get({'BOTSID':'LIN','totalNetPrice':None})})
            lout.put({'BOTSID':'lineItems','netPrice':lin.get({'BOTSID':'LIN','netPrice':None})})
            lout.put({'BOTSID':'lineItems','orderNumber':lin.get({'BOTSID':'LIN','orderNumber':None})})
            lout.put({'BOTSID':'lineItems','taxRate':lin.get({'BOTSID':'LIN','taxRate':None})})
