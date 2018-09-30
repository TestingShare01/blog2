# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.

#admin.site.register(banners)
#admin.site.register(Article)
admin.site.register(Classify)
admin.site.register(TimeLife)
from django.contrib import admin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('Article_title',"Article_author","Article_classify","Article_time","Article_readNum","Article_likeNum")

    class Media:
        js = (
            '/static/js/editor/kindeditor3/kindeditor-all.js',
            '/static/js/editor/kindeditor3/kindeditor/lang/zh-CN.js',
            '/static/js/editor/kindeditor3/config.js',
        )

@admin.register(banners)
class bannerAdmin(admin.ModelAdmin):
    list_display = ("images","content","banner_url")


@admin.register(heardyou)
class heardyouAdmin(admin.ModelAdmin):
    list_display = ("images", "content", "banner_url")

