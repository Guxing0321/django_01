# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from .models import *


# Create your views here.
def index(request):
    # temp = loader.get_template('test1/index.html')
    booklist = BookInfo.objects.all()
    context = {'title': '南京信息工程大学','booklist':booklist}
    return render(request, 'test1/index.html', context)


# 返回到show的页面
def show(request,id):
    return  render(request,'test1/show.html')