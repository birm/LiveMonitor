#the driving engine for host checks
class HostMonitor:
    #need netaddr
    __metaclass__=MonitorRegistry
    status=[] #last changes
    prev=[]
    subnet="192.168.1.0/24" # the subnet range string 
    sub=IPSet(["192.168.1.0/24"]) # the object to iterate through   
    freq=10 # how often to check in seconds
    self.safe=True

    def __init__(self,subnet="192.168.1.0/24",freq=10):
        #ensure variables are correct type
        self.subnet=subnet
        self.freq=freq
        self.sub=IPSet([subnet])
        self.worker=threading.Timer(self.freq,self.check)
        
    def check():
        tmp=self.status
        self.safe=False
        self.status=[]
        for address in sub:
            self.status[address]=#get status
        self.prev=tmp
        self.safe=True

    def start():
        self.worker.start()
