def envelopecontent(ta_info, out, *args, **kwargs):
    out.put({'BOTSID':'UNB', '0032':'EANCOM'})

def ta_infocontent(ta_info, *args, **kwargs):
    ta_info['UNB.S002.0007'] = '09'
