from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "WhatTo.Eat is on its way!"}
    return render(request, 'whatToEat/index.html', context_dict)

def about(request):
    context_dict = ""
    return render(request, 'WhatToEat/about.html', context_dict)

