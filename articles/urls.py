from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'articles'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('article/<int:article_id>/', views.article_view, name="article"),
    path('new_article/', views.new_article_view, name="new_article"),
    path('edit_article/<int:article_id>/', views.edit_article_view, name="edit_article"),
    path('delete_article/<int:article_id>/', views.delete_article_view, name="delete_article"),

]