#coding-utf-8
import requests,re,json,html2text,sys,time,os
from bs4 import BeautifulSoup
from array import array
import time 
from urllib.request import urlretrieve
from urllib import request

root = os.path.abspath('.')
baseFileName = 'no.txt'
baseFilePath = os.path.join(root, baseFileName)

def getTopicList():
    with open(baseFilePath, 'r') as f:
        num=0
        for line in f.readlines():
            link = line.strip()
            fileName = link[link.rfind("/")+1:]
            try:
                os.rename(fileName, str(num)+'.jpg')
            except FileNotFoundError as e:
                pass
            num=num+1
    

def saveImage(imgUrl, num):
    req = request.Request(imgUrl)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    fileName = str(num)+'.jpg'
    path = r"F:\\CODE\\Python\\1\\"+fileName  
    urlretrieve(req,path)

def myDecodeFromHtml_gbk(text):
    b = array('b', text)
    c = b.tostring()
    d = c[::2]
    e = d.decode('gbk')
    return e
    
if __name__=="__main__":
    print('runing..............')
    getTopicList()
    time.sleep(2)
