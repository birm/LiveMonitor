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
