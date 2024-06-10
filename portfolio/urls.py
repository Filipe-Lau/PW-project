from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view, name='landing_page'),
    path('me_by_me', views.me_by_me_view, name='me_by_me'),
    path('sobre', views.sobre_view, name='sobre'),
    path('automacao', views.automacao_view, name='automacao'),

]