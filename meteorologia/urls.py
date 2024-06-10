from django.urls import path
from . import views

app_name = "meteorologia"

urlpatterns = [
    path('api/cidades/', views.api_lista_cidades, name='api_lista_cidades'),
    path('api/previsão/hoje/<int:city_id>/', views.api_tempo_hoje, name='api_tempo_hoje'),
    path('api/previsao/cinco_dias/<int:city_id>/', views.tempo_5_dias, name='api_tempo_5_dias'),
    path('tempo/hoje/lisboa/', views.tempo_hoje_lisboa, name='tempo_hoje_lisboa'),
    path('tempo/<int:city_id>/', views.tempo_hoje, name='tempo_hoje'),
    path('previsao/<int:city_id>/', views.tempo_5_dias, name='tempo_5_dias'),
    path('', views.cidades, name='cidades'),

]