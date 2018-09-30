# -*- coding: utf-8 -*-
import editor
import lxml
from bs4 import BeautifulSoup
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def titlelong(values):
    """首页标题过长，截断显示70个字"""
    if len(values)>70:
        return values[:65]+"..."
    else:
        return values

@register.filter
def titleshortlong(values):
    """文章标题显示40个字"""
    if len(values)>40:
        return values[:39]+"..."

@register.filter
def readlong(values):
    """点赞超过9999，显示9999+"""
    if values>9999:
        return "9999+"
    else:
        return values

@register.filter
def retint(values):
    """忘记了"""
    return int(values)


@register.filter
def retwenzi(values):
    """mark_safe干嘛的忘记了，稍后学习下"""
    return mark_safe(values)

@register.filter
def contenctslong(values):
    if len(values)>100:
        return values[:140]+"..."
    else:
        return values

@register.filter
def retmeiyougengduole(values):
    print "----》value{}".format(values)
    print "-----type{}".format(values)
    if values is None:
        return "没有更多了"


@register.filter
def reteditor(values):
    """对于文章内容数据库存储了对应的标签，前端在显示的时候显示标签了
        这里对标签进行处理，直接获取文本，调用get_text()获取文本
    """
    B = BeautifulSoup(values)
    con = B.find().get_text()
    return con