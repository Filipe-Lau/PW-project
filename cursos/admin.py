from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Curso
from .models import Docente
from .models import Linguagem_de_programacao
from .models import Projeto
from .models import Disciplina

admin.site.register(Curso)
admin.site.register(Docente)
admin.site.register(Linguagem_de_programacao)
admin.site.register(Projeto)
admin.site.register(Disciplina)