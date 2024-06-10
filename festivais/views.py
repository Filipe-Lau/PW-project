from django.shortcuts import render
from .models import *

def index_view(request):
    context = {
        'localizacao': Localizacao.objects.all(),
        'festivais_Lisboa': Festival.objects.filter(localizacao__cidade = 'Lisboa'),
        'festivais_Zambujeira_do_Mar': Festival.objects.filter(localizacao__cidade = 'Zambujeira do Mar'),
        'bandas': Banda.objects.all().order_by('nome'),
    }
    return render(request,'festivais/festivais.html',context)


def festival_view(request,festival_id):
    context = {
        'festival': Festival.objects.get(id=festival_id),
        'bandas': Banda.objects.filter(festival = festival_id).order_by('nome'),
    }
    return render(request,'festivais/festival.html',context)