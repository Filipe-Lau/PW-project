from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'


class Localizacao(models.Model):
    cidade = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.cidade}'

class Festival(models.Model):
    banda = models.ManyToManyField(Banda)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capa_festivais/', blank=True)

    def __str__(self):
        return f'{self.nome}'