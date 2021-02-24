#coding-utf-8
import requests,re,json,html2text,sys,time,urllib.parse
from bs4 import BeautifulSoup
from array import array
import time 
from urllib.request import urlretrieve
import os
import chardet

sys.setrecursionlimit(1000000) #例如这里设置为一百万
url="http://www.t66y.com/htm_data/2003/7/3848132.html"
path = 'D:\\1111\\'
  

    
class ContextDownLoader(object):

    def __init__(self, link, path='D:\\1111\\'):
        # print(link)
        self.link = link
        self.path = path
        self.errLineNum = 0
    
    def setLink(self,link):
        self.link = link
        return self
    
    def getLink(self):
        return self.link

    def setPath(self,path):
        self.path = path
        return self
    
    def getPath(self):
        return self.path
        
    def getErrLineNum(self):
        return self.errLineNum
    
    def downHtmlCont(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER','Connection':'keep-alive'}
        while True:
            try:
                get_url = requests.get(self.link, headers=headers)
                break
            except requests.exceptions.ContentDecodingError as e:
                print('requests.exceptions.ContentDecodingError...')
                time.sleep(5)
                continue
            except requests.exceptions.ProxyError as e:    
                print('equests.exceptions.ProxyError...')
                time.sleep(5)
                continue
            except requests.packages.urllib3.exceptions.ProtocolError as e:    
                print('requests.packages.urllib3.exceptions.ProtocolError...')
                time.sleep(5)
                continue
            except requests.exceptions.ConnectionError as e:    
                print('requests.exceptions.ConnectionError...')
                time.sleep(5)
                continue
        codingTypr = get_url.encoding
        soup = BeautifulSoup(get_url.text,"html5lib")
        titleList = soup.find_all("title")
        try:
            title = titleList[0].string.encode(codingTypr, errors='ignore').decode('gbk', errors='ignore')
            #title = title.split('技術討論區')[0]
            title = title[0:title.rfind('技術討論區')]
        except IndexError as e:
            return False
        print('down loading:%s'%(title))
        fpath = self.path+title+'.html'

        try:
            fo = open(fpath, 'w+')
            fo.write('<title>%s</title>\n'%(self.link))
        except OSError as e:
            print('##FAIL##')
            return False
        imgList = soup.find_all("div", class_="tpc_content do_not_catch")
        imgSrcList = []
        for i in imgList:
            #mod a link
            linkList = i.find_all("a", target="_blank")
            for j in linkList:
                if j.string and j.string.find('www') != -1:
                    j["href"] = j.string
            #mod img link    
            imgList = i.find_all("img")
            for j in imgList:
                del j["onclick"]
                # print(j)
                elemList = ['src', 'data-src', 'ess-data', 'data-ess', 'data-ssa', 'data-sss']
                isMatch = False
                for m in elemList:
                    if j.has_attr(m):
                        j["src"] = j[m]
                        imgSrcList.append(j[m])
                        isMatch = True
                        break
                if not isMatch:
                    print(self.link)
                    print(j.encode(codingTypr, errors='ignore').decode('gbk', errors='ignore'))
            xmlText = i.encode(codingTypr, errors='ignore').decode('gbk', errors='ignore')
            if xmlText.find("牋") != -1:
                xmlText = i.encode(codingTypr, errors='ignore').decode('GB2312', errors='ignore')
            try:
                fo.write('%s\n'%(xmlText))
            except UnicodeEncodeError as e:
                self.errLineNum = self.errLineNum + 1
                continue
        try:
            fo.write('<textarea rows="%d" cols="500" readonly="readonly">\n'%(len(imgSrcList)))
        except OSError as e:
            return False
        if len(imgSrcList) > 0:
            try:
                for i in imgSrcList:
                    fo.write('%s\n'%(i.encode(codingTypr, errors='ignore').decode('gbk', errors='ignore')))
            except Exception as e:
                print(e)
                return False
        try:
            fo.write('</textarea>\n')
        except OSError as e:
            return False
            
        fo.close()  
        return True
        
        
if __name__=="__main__":
    print('runing..............')
    a = ContextDownLoader(url)
    a.downHtmlCont()
    print('done')        
        
        
        
        
        
        
        
        
        