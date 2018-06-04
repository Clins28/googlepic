import requests
from bs4 import BeautifulSoup
import threading
import lxml

class DoSoup:
    url = []
    html = []
    result = []
    def __init__(self, url):
        self.url = url
        self.html = self.gethtml(self.url)
        
    def gethtml(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'
            ,
            'Cookie': 'bid=I0klBiKF3nQ; ll="118277"; gr_user_id=ffdf2f63-ec37-49b5-99e8-0e0d28741172; ap=1; _vwo_uuid_v2=8C5B24903B1D1D3886FE478B91C5DE97|7eac18658e7fecbbf3798b88cfcf6113; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1498305874%2C%22https%3A%2F%2Fbook.douban.com%2Ftag%2F%25E9%259A%258F%25E7%25AC%2594%3Fstart%3D20%26type%3DT%22%5D; _pk_id.100001.4cf6=4e61f4192b9486a8.1485672092.5.1498306809.1498235389.; _pk_ses.100001.4cf6=*'
        }
        req = requests.get(url, headers)
        return req.text
        
    def getobject(self):
        print("This is a father class, try to inhert this class")
    
class DoDownload:

    downloadurl = []    # a list of download object
    savepath = []
    thread = 1
    
    def __init__(self, thread, downloadurl):
        self.thread = thread
        self.downloadurl = downloadurl
        
    def download(self, url, savepath):
        urllib.request.urlretrieve(url, filename=savepath)

    def trydownload(self)
        threads = []
        if self.thread == 1:
            for i in range(len(self.downloadurl)):
                self.download(self.downloadurl[i], self.savepath[i])
        else:
            for i in range(thread):
                t = threading.Thread(target = download, args = (i, url, savepath))
                threads.append(t)
                t.start()
                
    def setsavepath(self):
        print("This is a father class, try to inhert this class")

    