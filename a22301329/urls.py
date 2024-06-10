from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),
    path('pwsite/', include('pwsite.urls')),
    path('novaapp/', include('novaapp.urls')),
    path('bandas/', include('bandas.urls')),
    path('articles/', include('articles.urls')),
    path('cursos/', include('cursos.urls')),
    path('festivais/', include('festivais.urls')),
    path('autenticação/', include('autenticação.urls')),
    path('', include('portfolio.urls')),
    path('meteorologia/', include('meteorologia.urls')),

]
