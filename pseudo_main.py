#imports
import threading

#classes

#Keep track of which monitors exist, so we can run them all
class MonitorRegistry(type):
    registry={} #keep track of things we need to register
    def __new__(cls,name,base,attributes)
        the_item=type.__new__(cls,name,base,attributes)
        cls.registry[theitem.__name__]=the_item
        return the_item

    @classmethod
    def whos(item):
        return dict(item.registry)

#the driving engine for port checks
class PortMonitor:
    #need socket
    __metaclass__ = MonitorRegistry
    status=[] #output variable of status at last check
    prev=[] #previous result, for comparison
    host="127.0.0.1" #the host to check
    ports=[80,22] # a list of ports to check
    freq=10 # how often to check, seconds
    safe=True

    def __init__(self,host="127.0.0.1",freq=10,ports=[80,22]):
        #ensure variables are correct type
        self.host=host
        self.freq=freq
        self.ports=ports
        self.worker=threading.Timer(self.freq,self.check)
        #open connection

    def __del__():
        #remove from registry
        #close connection

    def check():
        tmp=self.status
        self.safe=False
        self.status=#perform a check on the ports
        self.prev=tmp
        self.safe=True

    def start():
        self.worker.start()

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

class LogMonitor:
    #need the scp thing
    #maybe a library to do logs
    __metaclass__=MonitorRegistry
    status=[]
    prev=[]
    fetch_params=[] #store ordered information for fetch
    freq=100
    safe=True
    
    def __init__(self,freq=100,fetch=self.scp_fetch,parse=self.json_parse,fetch_params=[]):
        self.fetch=fetch
        self.parse=parse
        self.fetch_params=fetch_params
        self.worker=threading.Timer(self.freq,self.check)
    
    def scp_fetch():
        #expecting host, path, and and auth type, then auth object?
        self.fetch_params
        #connect to host
        #get text
        return raw_text
    
    def json_parse(raw_text):
        self.parse_params
        #expecting parent, number to go back, and unique id
        #if parent="/" or something,  then it's the whole document
        #if not, get content of records whose unique id aren't already stored
    
    def check():
        tmp=self.status
        self.safe=False
        self.status=self.parse(self.fetch())
        self.prev=tmp
        self.safe=True
                
    def start():
        self.worker.start()       

#api rendering stuff
