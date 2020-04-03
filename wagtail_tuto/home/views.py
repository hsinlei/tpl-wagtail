# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import CopyWritingSettings
from blog.models import PostPage

def home(request):
    social_media_setting = PostPage.objects.live()
    context = {'social_media_setting': social_media_setting}
    return render(request, 'home/home_page.html', context=context)
