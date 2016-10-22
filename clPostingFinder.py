#coding-utf-8
import requests,re,json,html2text,sys,time,urllib.parse
from bs4 import BeautifulSoup
from array import array
import time 
from urllib.request import urlretrieve
import os
from clDownHtml import ContextDownLoader

url_source="http://www.t66y.com/thread0806.php?fid=7&search=&page="
posting_url_title="http://www.t66y.com/"
keyWord = '校园'
path = 'D:\\1111\\1.txt'
isFliter = 0

def getTopicList():
    with open(path, 'w') as f:
        f.write('结果:\n')
    for pageNum in range(2,3):
        url=url_source+str(pageNum)
        get_url = requests.get(url)
        codingTypr = get_url.encoding
        soup = BeautifulSoup(get_url.text,"html.parser")
        tdList = soup.find_all("h3")
        for i in tdList:
            title = i.a.string.encode(codingTypr, errors='ignore').decode('gbk', errors='ignore')
            if 1 == isFliter :
                if keyWord in title:
                    print('标题:%s, 连接: %s'%(title, posting_url_title+i.a.get('href')))
                    with open(path, 'a') as f:
                        f.write('标题:%s, 连接: %s\n'%(title, posting_url_title+i.a.get('href')))
            else:
                dl = ContextDownLoader(posting_url_title+i.a.get('href'))
                dl.downHtmlCont()
        time.sleep(1)

if __name__=="__main__":
    getTopicList()