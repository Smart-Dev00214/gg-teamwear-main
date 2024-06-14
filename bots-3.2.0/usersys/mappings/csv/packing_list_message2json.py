def main(inn,out):
    for sin in inn.getloop({'BOTSID':'SHP'}):
        out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','documentNumber':sin.get({'BOTSID':'SHP','documentNumber':None})})
        for ain in sin.getloop({'BOTSID':'SHP'},{'BOTSID':'ADR'}):
            out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','shipToGLN':ain.get({'BOTSID':'ADR','shipToGLN':None})})
            out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','shipToName':ain.get({'BOTSID':'ADR','shipToName':None})})
            out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','shipToAddressLine1':ain.get({'BOTSID':'ADR','shipToAddressLine1':None})})
            out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','shipToAddressLine2':ain.get({'BOTSID':'ADR','shipToAddressLine2':None})})
            out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','shipToCity':ain.get({'BOTSID':'ADR','shipToCity':None})})
            out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','shipToCountryCode':ain.get({'BOTSID':'ADR','shipToCountryCode':None})})
            out.put({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES','shipToPostalCode':ain.get({'BOTSID':'ADR','shipToPostalCode':None})})

        for pin in sin.getloop({'BOTSID':'SHP'},{'BOTSID':'PAC'}):
            pout = out.putloop({'BOTSID':'ROOT'},{'BOTSID':'MESSAGES'},{'BOTSID':'packages'})
            pout.put({'BOTSID':'packages','packageNumber':pin.get({'BOTSID':'PAC','packageNumber':None})})
            pout.put({'BOTSID':'packages','weight':pin.get({'BOTSID':'PAC','weight':None})})
            pout.put({'BOTSID':'packages','width':pin.get({'BOTSID':'PAC','width':None})})
            pout.put({'BOTSID':'packages','length':pin.get({'BOTSID':'PAC','length':None})})
            pout.put({'BOTSID':'packages','height':pin.get({'BOTSID':'PAC','height':None})})
            pout.put({'BOTSID':'packages','SSCC':pin.get({'BOTSID':'PAC','SSCC':None})})

            for lin in pin.getloop({'BOTSID':'PAC'},{'BOTSID':'LIN'}):
                lout = pout.putloop({'BOTSID':'packages'},{'BOTSID':'lineItems'})
                lout.put({'BOTSID':'lineItems', 'orderNumber':lin.get({'BOTSID':'LIN','orderNumber':None})})
                lout.put({'BOTSID':'lineItems', 'itemNumber':lin.get({'BOTSID':'LIN','itemNumber':None})})
                lout.put({'BOTSID':'lineItems', 'shippedQuantity':lin.get({'BOTSID':'LIN','shippedQuantity':None})})
                
