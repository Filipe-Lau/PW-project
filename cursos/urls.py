from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'cursos'

urlpatterns = [
    path('index/', views.cursos_view, name = 'index'),
    path('disciplinas/<int:disciplina_id>/', views.disciplinas_view, name = 'disciplinas'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name = 'disciplina'),
    path('novo_curso/<int:curso_id>/', views.novo_curso_view, name = 'novo_curso'),
    path('edita_curso/<int:curso_id>/', views.edita_curso_view, name = 'edita_curso'),
    path('apaga_curso/<int:curso_id>/', views.apaga_curso_view, name = 'apaga_curso'),
    path('nova_disciplina/<int:disciplina_id>/', views.nova_disciplina_view, name = 'nova_disciplina'),
    path('edita_disciplina/<int:disciplina_id>/', views.edita_disciplina_view, name = 'edita_disciplina'),
    path('apaga_disciplina/<int:disciplina_id>/', views.apaga_disciplina_view, name = 'apaga_disciplina'),

]