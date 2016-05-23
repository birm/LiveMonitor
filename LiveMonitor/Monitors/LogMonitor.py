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
        #get text, sftp
        return raw_text
    
    def json_parse(raw_text):
        self.parse_params
        #expecting parent, number to go back, and unique id
        #if parent="/" or something,  then it's the whole document
        #if not, get content of records whose unique id aren't already stored
        return result
    
    def check():
        tmp=self.status
        self.safe=False
        self.status=self.parse(self.fetch())
        self.prev=tmp
        self.safe=True
                
    def start():
        self.worker.start()       

