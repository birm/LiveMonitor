import logging, time, threading, json, subprocess
from MonitorRegistry import *
class LogMonitor:
    #maybe find a library to parse more formats?
    __metaclass__=MonitorRegistry
    status=[]
    prev=[]
    fetch_params=[] #store ordered information for fetch
    parse_params=[] #store ordered information for parse
    freq=100
    safe=True
    result={} #store your variables
    
    def __init__(self, **kwargs):
        self.fetch=kwargs.get('freq', 100)
	self.fetch=kwargs.get('fetch',self.scp_fetch)
        self.parse=kwargs.get('parse', self.json_parse)
        self.fetch_params=kwargs.get('fetch_params',[])
        self.parse_params=kwargs.get('parse_params',[])
        self.worker=threading.Timer(self.freq,self.check)
    
    def scp_fetch():
        #how cross compatible is this?
        #I guess they should haver certificates?
        #TODO figure out more robust way to get remote logs

        #expecting host, path, and and username in fetch_params
        host=self.fetch_params[0]
        path=self.fetch_params[1]
        uname=self.fetch_params[2]
        #get, cat, and return this text
        ssh=subprocess.Popen(['ssh', uname+'@'+host, 'cat', path],
                       stdout=subprocess.PIPE)
        #TODO warn for not found file
        #if ssh.stdout[0]="File Not Found": #is this empty or an ssh error on systems?
        #    log.warning("File " + path + " not found on " + host)
        result=""
        for text in ssh.stdout:
            result=result+text
        return result
    
    def json_parse(raw_text):
        #initalize result dictionary
        res={}
        #expecting parent and unique id in parse_params
        parent=self.parse_params[0]
        uid=self.parse_params[1]
        #whole document: we want everything, save to timestamp
        if (parent=="/"):
            res[str(int(time.time()))]=json.loads(raw_text)
        #if not, get content of records whose unique id aren't already stored
        else:
            full=json.loads(raw_text)[parent]
            for item in full:
                res[item[uid]]=item
        return res #dict type
    
    def check():
        tmp=self.status
        self.safe=False
        self.status.update(self.parse(self.fetch())) #expects dict of dicts
        self.prev=tmp
        self.safe=True
                
    def start():
        self.worker.start()       

