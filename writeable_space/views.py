from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(render(request,'writeable_space/home.html'))