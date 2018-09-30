# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bloggs import models
from django.shortcuts import render,HttpResponse,redirect
from mysites import settings
# Create your views here.
import os,uuid,json
import datetime as dt
from django.views.decorators.csrf import csrf_exempt
from common.newsxinlang import *
from django.core.paginator import Paginator
from PIL import ImageFile
import uuid
from common import visitNum
def index(request):
    """首页展示内容"""
    visitNum.change_info(request)
    banner = models.banners.objects.all()
    article = models.Article.objects.order_by("-Article_time")[:20]
    # date = models.Article.objectss.distinct_date()
    topic = models.heardyou.objects.all()
    pagess = request.GET.get("page")
    try:
        page = Paginator(article, 5)
        sheet_num = page.page_range
        weiye = sheet_num[-1]
        pages = page.page(pagess)
    except:
        pages = page.page(1)


    return render(request, "index.html", locals())


    """修改数据
    方式一
    banner_list = models.banners.objects.get(id=1).updata(字段1="数据1")

    方式二
    obj = models.banners.objects.get(id=1)
    obj.pwd = '520'
    obj.save()"""


    """删除数据
    banner_list = models.banners.objects.all().delete() #删除表中全部数据
    banners = models.banners.objects.get(id=1).delete() #删除表中id=1的数据"""


    """查看数据方式
    banner_list = models.banners.objects.all() #查询表banners全部数据返回list数据
    banners = models.banners.objects.get(id=1) #查询指定数据，id=1的数据，返回的是实例
    bannerss = models.banners.objects.filter(id=1) #查询指定数据，id=1的数据，返回的是QuerSet对象列表"""



    """增加数据的两种方式
    num = models.banners(images="aa",content="bb",banner_url="cc")
    num2 = models.banners.create(images="aa",content="bb",banner_url="cc")
    num.save()"""

def global_setting(request):
    """全局变量配置"""
    classify = models.Classify.objects.all()
    reads = models.Article.objects.order_by("-Article_readNum")[:5]
    likeNum = models.Article.objects.order_by("-Article_likeNum")[:1]

    return {
        "classify":classify,
        "reads":reads,
        "likeNum":likeNum

    }

def info(request, nid):
    """文章详情页数据"""
    info = models.Article.objects.get(id=nid)
    info.increase_views()
    nextID = int(nid)+1
    shangID = int(nid)-1
    try:
        nextcon = models.Article.objects.get(id=nextID)
    except:
        nextcon = models.Article.objects.get(id=nid)
    try:
        shangcon = models.Article.objects.get(id=shangID)
    except:
        shangcon = models.Article.objects.get(id=nid)

    # print "------》{}".format(int(nid))
    return render(request,"info.html",locals())

def list(request,id,pages):
    """分类，文章列表"""
    listArticle = models.Article.objects.all().filter(Article_classify=id)
    classifyList = models.Classify.objects.all().filter(id=id)
    try:
        page = Paginator(listArticle,10)
        sheet_num = page.page_range
        weiye = sheet_num[-1]
        pages = page.page(pages)
    except:
        pages = page.page(1)

    return render(request,"list.html",locals())


def newspaper(request):
    """前端新闻页面，抓取两个页面的内容，存入数据库，展示前端"""
    xinlang()
    pyluntan()
    classifys = request.GET.get("classifys")
    pagess = request.GET.get("page")
    if classifys == "xinlang":
        paper = models.Newpaper.objects.all().filter(Newpaper_classify="新浪").order_by("-Newpaper_time")
        try:
            page = Paginator(paper, 10)
            sheet_num = page.page_range
            weiye = sheet_num[-1]
            pages = page.page(pagess)
        except:
            pages = page.page(1)

        return render(request, "gbook.html", locals())
    elif classifys == "pyshe":
        paper = models.Newpaper.objects.all().filter(Newpaper_classify="py社区").order_by("-Newpaper_time")[:100]
        try:
            page = Paginator(paper, 20)
            sheet_num = page.page_range
            pages = page.page(pagess)
        except:
            pages = page.page(1)

        return render(request,"gbook.html",locals())

def times(request):
    """前端时间轴页面，暂时不用，html页面存在问题，没解决"""
    TimeTitle= models.TimeLife.objects.order_by("-Time_time")
    return render(request,"time.html",locals())

def test(request):
    return render(request,"test.html")


def tupians(request):
    """测试图片上传"""
    if request.method == "POST":
        f1 = request.FILES['testimg']
        fname = '%s/%s' % (settings.MEDIA_ROOT, f1.name)
        print "图片地址--》{}".format(fname)
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
        return render(request, "tupians.html")
    else:
        return render(request,"tupians.html")


def listdata(request):
    """展示文章列表，更改前端展示图片"""
    articleall = models.Article.objects.order_by("-Article_time")
    banner = models.banners.objects.all()
    VisitNumber = models.VisitNumber.objects.all()
    Userip = models.Userip.objects.all()
    DayNumber=models.DayNumber.objects.all()
    try:
        res = request.GET.get("del")
        print "res--->{}".format(res)
        article = models.Article.objects.get(id = res).delete()
    except:
        pass

    if request.method == "POST":
        f1 = request.FILES['testimg']
        fid = request.POST.get("id")
        parser = ImageFile.Parser()
        file_suffix = f1.name.split('.')[-1]
        f1.name = str(uuid.uuid1()) + '.' + file_suffix
        for chunk in f1.chunks():
            parser.feed(chunk)
        img = parser.close()
        name = '%s%s' % (settings.MEDIA_ROOT, f1.name)  ##这里的时保存文件的路径加名字！

        sqlNamePhone = "/static/media/"+f1.name
        img.save(name)
        p = models.Article.objects.get(id = fid)
        p.Article_images = sqlNamePhone
        p.save()

        return render(request, "listdata.html", locals())

    else:

        return render(request,"listdata.html",locals())