#coding-utf-8
import requests,re,json,html2text,sys,time,urllib.parse
from bs4 import BeautifulSoup
from array import array
import time 
from urllib.request import urlretrieve
import os

url="http://www.t66y.com/htm_data/7/1610/2116257.html"
path = 'D:\\2222\\'

def getTopicList():
    if not os.path.isdir(path):
        os.mkdir(path)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    while True:
        try:
            get_url = requests.get(url, headers=headers)
            break
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
    titleList = soup.find_all("title")
    title = titleList[0].string.encode(codingTypr, errors='ignore').decode('gbk', errors='ignore').split('草')[0]
    fpath = path+title+'.txt'
    with open(fpath, 'w') as f:
        f.write('')
    imgList = soup.find_all("img", style='cursor:pointer')
    num = 1
    for i in imgList:
        print('第%d幅图:%s'%(num,i.get('src')))
        with open(fpath, 'a') as f:
            f.write('%s\n'%(i.get('src')))

if __name__=="__main__":
    getTopicList()