#coding-utf-8
import requests,re,json,html2text,sys,time,urllib.parse
from bs4 import BeautifulSoup
from array import array
import time 
from urllib.request import urlretrieve
import os

sys.setrecursionlimit(1000000) #例如这里设置为一百万
url="http://www.t66y.com/htm_data/7/1610/2110560.html"
path = 'D:\\1111\\'
  

    
class ContextDownLoader(object):

    def __init__(self, link, path='D:\\1111\\'):
        self.link = link
        self.path = path
    
    def setLink(self,link):
        self.link = page
        return self
    
    def getLink(self):
        return self.link

    def setPath(self,path):
        self.path = path
        return self
    
    def getPath(self):
        return self.path
    
    def downHtmlCont(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
        get_url = requests.get(self.link, headers=headers)
        codingTypr = get_url.encoding
        soup = BeautifulSoup(get_url.text,"html5lib")
        titleList = soup.find_all("title")
        title = titleList[0].string.encode(codingTypr, errors='ignore').decode('gbk', errors='ignore').split('草')[0]
        print('down loading:%s'%(title))
        fpath = self.path+title+'.html'
        try:
            with open(fpath, 'w') as f:
                f.write('')
            with open(fpath, 'a') as f:
                f.write('<title>%s</title>\n'%(self.link))
        except OSError as e:
            return
        imgList = soup.find_all("div", class_="tpc_content do_not_catch")
        for i in imgList:
            xmlText = i.encode(codingTypr, errors='ignore').decode('gbk', errors='ignore')
            try:
                with open(fpath, 'a') as f:
                    f.write('%s\n'%(xmlText))
            except OSError as e:
                return
        
        
        
        
if __name__=="__main__":
    print('runing..............')
    a = ContextDownLoader(url)
    a.downHtmlCont()
    print('done')        
        
        
        
        
        
        
        
        
        