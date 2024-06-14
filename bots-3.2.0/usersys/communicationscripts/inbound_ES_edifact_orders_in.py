from django.utils.translation import ugettext as _

import bots.botslib as botslib
import bots.communication as communication

class sftp(communication.sftp):
    def connect(self):
        ''' Override regular sftp for Amazon. Need to disable Paramiko transport
            pubkey algorithms because Amazon doesn't list supported pubkey algorithms.
            https://stackoverflow.com/questions/70565357/paramiko-authentication-fails-with-agreed-upon-rsa-sha2-512-pubkey-algorithm
        '''
        # check dependencies
        try:
            import paramiko
        except:
            raise ImportError(_(u'Dependency failure: communicationtype "sftp" requires python library "paramiko".'))
        try:
            from Crypto import Cipher
        except:
            raise ImportError(_(u'Dependency failure: communicationtype "sftp" requires python library "pycrypto".'))

        # Get hostname and port to use
        hostname = self.channeldict['host']
        try:
            port = int(self.channeldict['port'])
        except:
            port = 22 # default port for sftp

        if self.userscript and hasattr(self.userscript,'hostkey'):
            hostkey = botslib.runscript(self.userscript,self.scriptname,'hostkey',channeldict=self.channeldict)
        else:
            hostkey = None
        if self.userscript and hasattr(self.userscript,'privatekey'):
            privatekeyfile,pkeytype,pkeypassword = botslib.runscript(self.userscript,self.scriptname,'privatekey',channeldict=self.channeldict)
            if pkeytype == 'RSA':
                pkey = paramiko.RSAKey.from_private_key_file(filename=privatekeyfile,password=pkeypassword)
            else:
                pkey = paramiko.DSSKey.from_private_key_file(filename=privatekeyfile,password=pkeypassword)
        else:
            pkey = None

        if self.channeldict['secret']:  #if password is empty string: use None. Else error can occur.
            secret = self.channeldict['secret']
        else:
            secret = None
        # now, connect and use paramiko Transport to negotiate SSH2 across the connection
        self.transport = paramiko.Transport((hostname,port),disabled_algorithms=dict(pubkeys=["rsa-sha2-512", "rsa-sha2-256"]))
        self.transport.connect(username=self.channeldict['username'],password=secret,hostkey=hostkey,pkey=pkey)
        self.session = paramiko.SFTPClient.from_transport(self.transport)
        channel = self.session.get_channel()
        channel.settimeout(10)
        self.set_cwd()

def privatekey(channeldict):
    return [channeldict['keyfile'],'RSA',None]
