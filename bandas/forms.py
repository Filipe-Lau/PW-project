from django import forms
from .models import Banda, Album, Musica
from django.contrib.auth.models import User

class UserRegistrationFrom(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username','first_name','last_name','email','password']

    widgets = {'password':forms.PasswordInput}


class BandaForm(forms.ModelForm):
    foto = forms.ImageField(required=False)
    class Meta:
        model = Banda
        fields = '__all__'

        help_texts = {
            'nome': 'Insira o nome da banda.',
            'nacionalidade': 'Insira a nacionalidade da banda.',
            'genero': 'Escolha o gênero musical da banda.',
            'ano': 'Insira o ano de formação da banda.',
            'foto': 'Insira uma fotografia da banda(não é obrigatório).',
        }

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'
    help_texts = {
            'banda': 'Insira o nome da banda.',
            'titulo': 'Insira o titulo do album.',
            'ano': 'Insira o ano de lançamento.',
            'capa': 'Insira uma fotografia da capa do album(não é obrigatório).',
        }

class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica
    fields = '__all__'
    help_texts = {
            'album': 'Insira o nome do album.',
            'titulo': 'Insira o titulo da música.',
            'duracao': 'Insira a duração.',
            'spotify_link': 'Insira o link do spotify.',
            'letra': 'Insira a letra da música',
            'bio': 'Escreva uma biografia da banda',
        }