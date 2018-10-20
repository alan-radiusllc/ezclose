# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello from EZ-Close. <a href='/ezclose/about/'> About</a>")
    context_dict = {'boldmessage': "crunchy!"}
    return render(request, 'ezclose/index.html', context=context_dict)
    
def about(request):
    #return HttpResponse("This is the about! <a href='/ezclose/'> Index</a>")
    context_dict = {'italicmessage': "crispy!"}
    return render(request, 'ezclose/about.html', context=context_dict)