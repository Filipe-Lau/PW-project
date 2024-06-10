from django.db import models


class Curso(models.Model):
    apresentacao = models.CharField(max_length = 100)
    objetivos = models.TextField()
    competencias = models.TextField()


class Area_Cientifica(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 100)

class Docente(models.Model):
    nome = models.CharField(max_length = 100)
    departamento = models.CharField(max_length = 100)
    email = models.EmailField()
    telefone = models.CharField(max_length = 15, blank = True, null = True)

    def str(self):
        return f'{self.nome}'

class Linguagem_de_programacao(models.Model):
    nome = models.CharField(max_length = 100)

    def str(self):
        return f'{self.nome}'

class Disciplina(models.Model):
    nome = models.CharField(max_length = 100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length = 100)
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length = 100)
    area_cientifica = models.ForeignKey(Area_Cientifica, on_delete=models.CASCADE)
    linguagem_usada = models.ManyToManyField(Linguagem_de_programacao, related_name = 'disciplinas')
    docente = models.ManyToManyField(Docente, related_name = 'disciplinas')

    def str(self):
        return f'{self.nome} - {self.docente.nome}'

class Projeto(models.Model):
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE, related_name = 'projetos')
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem = models.ImageField('projeto_imagem/')
    youtube_link = models.URLField(null = True, blank=True)
    github_link = models.URLField(null = True, blank=True)
    linguagem_usada = models.ManyToManyField(Linguagem_de_programacao, related_name = 'projetos')

    def str(self):
        return f'{self.nome}'