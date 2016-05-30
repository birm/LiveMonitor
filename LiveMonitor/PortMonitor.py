import logging, threading, socket
from Monitor import *
#the driving engine for port checks
class PortMonitor(Monitor):
    #need socket
    status={} #output variable of status at last check
    prev={}
    safe=True
    timeout= 0.1

    def __init__(self,**kwargs):
        super(self.__class__,self).__init__(self,**kwargs)
        self.host=kwargs.get('host',"127.0.0.1")
        self.freq=kwargs.get('freq',10.0)
        self.ports=kwargs.get('ports',[80,22])
        self.worker=threading.Timer(self.freq,self.check)
        self.__repr__="Port Monitor for " + self.host
        #runtime checks
        if (self.freq<(len(self.ports)*self.timeout)):
            #recommend reconfiguring timeout
            log.warning("Your timeout ("+self.freq+"s) may be set to be too slow to scan "+ len(self.ports)+" ports every " + self.freq +" seconds. Set with .timeout")

    def check():
        try:
            newstatus=[]
            #pick a timeout fast so that it can finish within (freq) seconds
            socket.settimeout(self.timeout)
            #perform a check on the ports
            for port in self.ports:
                #create socket to check port
                active = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if(sock.connect_ex((self.host, port))):
                    #nonzero return means closed
                    newstatus.append(False)
                else:
                    #zero means it's open
                    newstatus.append(True)
                #close socket to check port
                active.close()
        except socket.error:
            #socket may have other errors I'm not expecting, but...
            log.error("Couldn't (re)connect to server at " + self.host)
            #to represent this error to any API
            newstatus="connection error"
        finally:
            #update variables
            self.safe=False
            tmp=self.status
            self.status=newstatus
            self.prev=tmp
            self.safe=True

    def start():
        self.worker.start()
