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
endNum = 4

def getTopicList():
    curNum = startNum
    if not isFliter == 0:
        filePathName = path+keyWord+'_result'
        if not os.path.isdir(filePathName):
            os.mkdir(filePathName)
    while curNum <= endNum:
        print('第%d页'%(curNum))
        url=url_source+str(curNum)
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER','Connection':'keep-alive'}
            get_url = requests.get(url,headers=headers)
            #print(dir(get_url))
            #print(get_url.text)
        except requests.exceptions.ContentDecodingError as e:
            print('requests.exceptions.ContentDecodingError...')
            time.sleep(1)
            continue
        except requests.exceptions.ProxyError as e:    
            print('equests.exceptions.ProxyError...')
            time.sleep(1)
            continue
        except requests.packages.urllib3.exceptions.ProtocolError as e:    
            print('requests.packages.urllib3.exceptions.ProtocolError...')
            time.sleep(1)
            continue
        except requests.exceptions.ConnectionError as e:    
            print('requests.exceptions.ConnectionError...')
            time.sleep(1)
            continue
        codingTypr = get_url.encoding
        soup = BeautifulSoup(get_url.text,"html.parser")
        tdList = soup.find_all("h3")
        print("len(tdList)=%d"%(len(tdList)))
        item_count = 1
        for i in tdList:
            title = i.a.string.encode(codingTypr, errors='ignore').decode('gbk', errors='ignore')
            if 1 == isFliter :
                if keyWord in title:
                    dl = ContextDownLoader(posting_url_title+i.a.get('href'), filePathName+'\\')
                    dl.downHtmlCont()
            else:
                print('第%d页|第%d篇|共%d篇|进度%4.2f%%'%(curNum, item_count, len(tdList), 100*item_count/len(tdList)),end='\r')
                dl = ContextDownLoader(posting_url_title+i.a.get('href'))
                dl.downHtmlCont()
                item_count = item_count + 1
        time.sleep(1)
        curNum = curNum + 1
        

if __name__=="__main__":
    if len(sys.argv) > 1 and sys.argv[1]:
        keyWord = sys.argv[1]
        print('搜索关键字为%s'%(keyWord))
    getTopicList()