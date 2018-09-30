# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
from bloggs import models

def xinlang():
    """抓去新浪新闻中的几条数据新闻"""
    html = requests.get("http://news.sina.com.cn/")
    html.encoding="utf-8"
    con = html.text
    soup = BeautifulSoup(con,"html.parser")
    tit = soup.select(".ct_t_01")
    for i in tit:
        a = i.select("h1")[0].text
        b = i.select("a")[0]["href"]
        if models.Newpaper.objects.filter(Newpaper_title=a):
            pass
        else:
            a = models.Newpaper(Newpaper_title=a,Newpaper_url=b,Newpaper_classify="新浪")
            a.save()


def pyluntan():
    """抓取这个网站的python数据"""
    html = requests.get("http://www.python88.com/")
    html.encoding = "utf-8"
    con = html.text
    soup = BeautifulSoup(con, "html.parser")
    tit = soup.select(".item_title")

    for i in tit:
        a = i.text.split("\n")
        b = "http://www.python88.com"+i.select("a")[0]["href"]
        for k in a:
            if k is not "":
                print k
                if models.Newpaper.objects.filter(Newpaper_title=k):
                    pass
                else:
                    a = models.Newpaper(Newpaper_title=k,Newpaper_url=b,Newpaper_classify="py社区")
                    a.save()
            else:
                pass
