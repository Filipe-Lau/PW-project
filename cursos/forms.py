from django import forms
from .models import Curso, Area_Cientifica, Docente, Linguagem_de_programacao, Disciplina, Projeto


class CursoForm(forms.ModelForm):
    foto = forms.ImageField(required=False)
    class Meta:
        model = Curso
        fields = '__all__'


class Area_CientificaForm(forms.ModelForm):
  class Meta:
    model = Area_Cientifica
    fields = '__all__'


class DocenteForm(forms.ModelForm):
  class Meta:
    model = Docente
    fields = '__all__'


class Linguagem_de_programacaoForm(forms.ModelForm):
  class Meta:
    model = Linguagem_de_programacao
    fields = '__all__'


class DisciplinaForm(forms.ModelForm):
  class Meta:
    model = Disciplina
    fields = '__all__'


class ProjetoForm(forms.ModelForm):
    imagem = forms.ImageField(required=False)
    class Meta:
        model = Projeto
        fields = '__all__'