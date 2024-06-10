from django.shortcuts import render
from datetime import datetime
# Create your views here.


def index_view(request):
    return render(request, "pwsite/index.html",
    {'date': datetime.today().date})

def index_view1(request):
    return render(request, "pwsite/sobre.html",
    {'date': datetime.today().date})