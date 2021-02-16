#!/usr/bin/python3
# -*- coding: utf-8 -*-
#ライブラリーインポート
import requests 
from bs4 import BeautifulSoup
from time import sleep

#スクレイピング
class Scr():
    def __init__(self, urls):
        self.urls=urls

    def geturl(self):
        all_text=[]
        for url in self.urls:
            r=requests.get(url)
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            article1_content=soup.find_all("p")
            temp=[]
            for con in article1_content:
                out=con.text
                temp.append(out)
            text=''.join(temp)
            all_text.append(text)
            sleep(1)
        return all_text

sc=Scr(["https://www.tvkingdom.jp/chart/23.action"])
print(sc.geturl())