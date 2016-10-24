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
keyWord = '精华'
path = 'D:\\1111\\'
isFliter = 0
startNum = 1
endNum = 1

def getTopicList():
    curNum = startNum
    if not isFliter == 0:
        filePathName = path+keyWord+'_result'
        if not os.path.isdir(filePathName):
            os.mkdir(filePathName)
    while curNum <= endNum:
        print('第%d页\n'%(curNum))
        url=url_source+str(curNum)
        try:
            get_url = requests.get(url)
        except requests.exceptions.ContentDecodingError as e:
            print('网页读取错误正在重试...')
            time.sleep(1)
            continue
        except requests.exceptions.ProxyError as e:    
            print('网络连接错误正在重试...')
            time.sleep(1)
            continue
        codingTypr = get_url.encoding
        soup = BeautifulSoup(get_url.text,"html.parser")
        tdList = soup.find_all("h3")
        for i in tdList:
            title = i.a.string.encode(codingTypr, errors='ignore').decode('gbk', errors='ignore')
            if 1 == isFliter :
                if keyWord in title:
                    dl = ContextDownLoader(posting_url_title+i.a.get('href'), filePathName+'\\')
                    dl.downHtmlCont()
            else:
                dl = ContextDownLoader(posting_url_title+i.a.get('href'))
                dl.downHtmlCont()
        time.sleep(1)
        curNum = curNum + 1
        

if __name__=="__main__":
    if len(sys.argv) > 1 and sys.argv[1]:
        keyWord = sys.argv[1]
        print('搜索关键字为%s'%(keyWord))
    getTopicList()