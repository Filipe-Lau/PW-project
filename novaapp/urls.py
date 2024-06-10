from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('LeySoul/', views.Ley_Soul_view, name='LeySoul'),
    path('DavidBowie/', views.David_Bowie_view, name='DavidBowie'),
    path('Soundgarden/', views.Soundgarden_view, name='Soundgarden'),
]