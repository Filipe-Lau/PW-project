from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!\n")


def index_view1(request):
    return HttpResponse("HELLO WORLD!\n")


def index_view2(request):
    return HttpResponse(":)\n")


def index_view3(request):
    return HttpResponse(" .\n\t..\n\t...")
