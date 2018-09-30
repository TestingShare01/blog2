# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class banners(models.Model):
    """首页banner数据"""
    images = models.CharField(max_length=50) #图片地址
    content = models.CharField(max_length=100) #描述
    banner_url = models.CharField(max_length=50) #跳转的url

    class Meta:
        db_table = "banners"


class ArticleManager(models.Manager):

    def distinct_date(self):
        """功能：文章归档
           使用：Manager管理器，写一个管理器功能，直接可以调用使用，需要与objects进行关联，写在Article数据库下
                objects = ArticleManager()
        """
        distinct_date_list =[]
        date_list = self.values("Article_time")
        for date in date_list:
            date = date_list["Article_time"].strftime("%Y%m文章存档")
            if date not in distinct_date_list:
                distinct_date_list.append(date)

        return distinct_date_list



class Article(models.Model):
    """文章数据"""
    Article_title = models.CharField(max_length=50)
    Article_images = models.CharField(max_length=50)
    Article_content = models.TextField(null=True)#用来存储体积较大的文本
    Article_author = models.CharField(max_length=30)
    Article_classify = models.ForeignKey("Classify",to_field="id",default=1)
    Article_time = models.DateTimeField(auto_now_add=True) #专门用于存储时间，auto_now=True，当内容修改时，时间自动更新
    Article_readNum = models.PositiveIntegerField(default=0)
    Article_likeNum = models.IntegerField()

    def increase_views(self):
        #此方法用于浏览数增加
        self.Article_readNum += 1
        self.save(update_fields=["Article_readNum"])


    class Meta:
        db_table = "Article"

class art(models.Model):
    arts = models.TextField(null=True)

class Classify(models.Model):
    """分类表"""
    classify = models.CharField(max_length=30)

    class Meta:
        db_table = "Classify"

    def __str__(self):
        return "%s" % (self.classify)


class Newpaper(models.Model):
    """新闻表"""
    Newpaper_title = models.CharField(max_length=100)
    Newpaper_url = models.CharField(max_length=100)
    Newpaper_time = models.DateTimeField(auto_now=True)
    Newpaper_classify = models.CharField(max_length=50)
    class Meta:
        db_table = "Newpaper"

class TimeLife(models.Model):
    """时间轴表"""
    Time_tilte = models.CharField(max_length=50)
    Time_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "TimeLife"

class heardyou(models.Model):
    """首页banner右侧两个图片"""
    images = models.CharField(max_length=50) #图片地址
    content = models.CharField(max_length=100) #描述
    banner_url = models.CharField(max_length=50) #跳转的url
    class Meta:
        db_table = "heardyou"


#访问网站的ip地址和次数
class Userip(models.Model):
    ip=models.CharField(verbose_name='IP地址',max_length=30)    #ip地址
    count=models.IntegerField(verbose_name='访问次数',default=0) #该ip访问次数
    class Meta:
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip

#网站总访问次数
class VisitNumber(models.Model):
    count=models.IntegerField(verbose_name='网站访问总次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = '网站访问总次数'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)

#单日访问量统计
class DayNumber(models.Model):
    day=models.DateField(verbose_name='日期',default=timezone.now)
    count=models.IntegerField(verbose_name='网站访问次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = '网站日访问量统计'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.day)


