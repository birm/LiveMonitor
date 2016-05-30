from socket import *
import time, json
#Keep track of which monitors exist, so we can run them all
class Monitor(type):
    result={}
    registry=[] #keep track of things we need to register
    def __init__(self,*args,**kwargs):
        Monitor.registry.append(self)

    @classmethod
    def whos(item):
        return dict(item.registry)

    @classmethod
    def start_all():
        for mon in registry:
            mon.start()
        
    @classmethod
    def get_status():
        for mon in registry:
            if mon.safe:
                self.result[repr(mon)]=mon.status
        return self.result
    
    @classmethod
    def serve():
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', 8080))
        serverSocket.listen(1)
        while True:
            message = connectionSocket.recv(1024)
            connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n')
            connectionSocket.send(json.dumps(Monitor.get_status()))
        try:
        finally:
            #keep going; I'll make a better http serv later
            pass
