from django.shortcuts import render

def index_view(request):

    return render(request,'portfolio/landing_page.html',)

def me_by_me_view(request):

    return render(request,'portfolio/me_by_me.html',)

def sobre_view(request):

    return render(request,'portfolio/sobre.html',)

def automacao_view(request):

    return render(request,'portfolio/automação.html',)