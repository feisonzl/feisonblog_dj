# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.

def Test(request):
    #return HttpResponse("just a test")
    #post = Article.objects.all()
    #return HttpResponse(post[0].content)
    return render(request, 'blog/test.html', {'current_time': datetime.now()})

def home(request):
    post_list = Article.objects.all()
    return render(request, 'blog/home.html',{'post_list':post_list})
    
def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/post.html',{'post':post})
