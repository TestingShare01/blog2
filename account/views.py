# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from . forms import Loginform
# Create your views here.

def user_login(request):
    if request.method =="POST":
        login_form = Loginform(request.POST) #传入前端数据，变成绑定数据的实例
        # print "login_from type-->{}".format(type(login_form))
        if login_form.is_valid(): #判断数据是否有效
            cd = login_form.clean() #返回字典类型的数据
            # print "cd---->{}".format(type(cd))
            user = authenticate(username=cd["username"],password=cd["password"]) # 获取到用户信息
            # print "user--->{}".format(user)
            if user: #判断用户是否有效真实
                login(request,user)
                return HttpResponse("successfully")
            else:
                return HttpResponse("No faile")

    if request.method =="GET":
        login_form=Loginform()
        return render(request,"account/login.html",{"form":login_form})