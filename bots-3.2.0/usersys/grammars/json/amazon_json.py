"""Common grammar parts file for the amazon_json grammar"""
from bots.botsconfig import *

def build_structure(message_structure):
    """Get the structure part of a JSON amazon grammar.

    :param message_structure: a list of dicts of any substructure that goes inside MESSAGES
    """
    return [
        {ID:'ROOT',MIN:1,MAX:1,
            QUERIES: {
                'frompartner': ({'BOTSID':'ROOT'},{'BOTSID':'HEADERS','interchangeSenderName':None}),
                'topartner': ({'BOTSID':'ROOT'},{'BOTSID':'HEADERS','interchangeRecipientName':None}),
            },
            LEVEL:[
                {ID:'HEADERS',MIN:0,MAX:1,},
                {ID:'MESSAGES',MIN:1,MAX:1,LEVEL:
                    message_structure,
                },
            ],
        }
    ]

def build_recorddefs(records):
    """Get the recorddefs part of a JSON amazon grammar.

    :param records: a dict of any extra records that make up the grammar.
    It must include the records in MESSAGES, as well as any records in the
    substructure. 
    """
    return dict({
        'ROOT':[
            ['BOTSID','M',4,'A'],
        ],
        'HEADERS':[
            ['BOTSID','M',7,'A'],
            ['interchangeSenderName','M',35,'A'],
            ['interchangeRecipientName','M',35,'A'],
            ['uniqueMessageReference','C',(1,14),'A'],
            ['messageTypeIdentifier','C',(1,6),'A'],
            ['messageTypeVersionNumber','C',(1,3),'A'],
            ['messageTypeControllingAgency','C',(1,2),'A'],
            ['associationAssignedCode','C',(1,6),'A'],
            ['numberOfMessageSegments','C',6,'N'],
        ],
    }, **records)
