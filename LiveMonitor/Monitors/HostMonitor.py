import logging, threading, subprocess, platform
#the driving engine for host checks
class HostMonitor:
    #need netaddr
    __metaclass__=MonitorRegistry
    status={} #last changes
    prev={}
    subnet="192.168.1.0/24" # the subnet range string 
    sub=IPSet(["192.168.1.0/24"]) # the object to iterate through   
    freq=10 # how often to check in seconds
    safe=True
    ping_suffix = "-c 1"

    def __init__(self,subnet="192.168.1.0/24",freq=10):
        self.subnet=subnet
        self.freq=freq
        self.sub=IPSet([subnet])
        self.worker=threading.Timer(self.freq,self.check)
        self.ping_suffix = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
        
    def check():
        tmp=self.status
        self.safe=False
        self.status={}
        for address in sub:
            self.status[address]=os.system("ping " + self.ping_suffix + " " + address)
            #TODO find exceptions for this?
            
        self.prev=tmp
        self.safe=True

    def start():
        self.worker.start()
