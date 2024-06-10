from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'novaapp/index.html')

def Ley_Soul_view(request):
    return render(request, 'novaapp/LeySoul.html')

def David_Bowie_view(request):
    return render(request, 'novaapp/DavidBowie.html')

def Soundgarden_view(request):
    return render(request, 'novaapp/Soundgarden.html')

