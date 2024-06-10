from django.shortcuts import render, redirect
from .models import Curso, Area_Cientifica, Docente, Linguagem_de_programacao, Disciplina, Projeto
from django.contrib.auth.decorators import login_required
from .forms import CursoForm, DisciplinaForm



def cursos_view(request):
    context = {
        'cursos': Curso.objects.all(),
    }

    return render (request, 'cursos/index.html', context)

def disciplinas_view(request, disciplina_id):
    context = {
        'disciplinas_1_ano': Disciplina.objects.filter(ano = 1).order_by('semestre'),
        'disciplinas_2_ano': Disciplina.objects.filter(ano = 2).order_by('semestre'),
        'disciplinas_3_ano': Disciplina.objects.filter(ano = 3).order_by('semestre'),
        'disciplina': Disciplina.objects.get(id = disciplina_id),
    }

    return render(request, 'cursos/disciplinas.html', context)


def disciplina_view(request, disciplina_id):
    context = {
        'disciplina': Disciplina.objects.get(id = disciplina_id),
    }

    return render(request, 'cursos/disciplina.html', context)


@login_required
def novo_curso_view(request):
    form = CursoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursos:index')

    context = {'form': form}
    return render(request, 'cursos/novo_curso.html', context)


@login_required
def edita_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)

    if request.POST:
        form = CursoForm(request.POST or None, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:index')
    else:
        form = CursoForm(instance=curso)

    context = {'form': form, 'curso':curso}
    return render(request, 'cursos/edita_curso.html', context)

@login_required
def apaga_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect('cursos:index')

@login_required
def nova_disciplina_view(request):
    form = DisciplinaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursos:index')

    context = {'form': form}
    return render(request, 'cursos/nova_disciplina.html', context)


@login_required
def edita_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)

    if request.POST:
        form = DisciplinaForm(request.POST or None, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('cursos:index')
    else:
        form = DisciplinaForm(instance=disciplina)

    context = {'form': form, 'disciplina':disciplina}
    return render(request, 'cursos/edit_disciplina.html', context)

@login_required
def apaga_disciplina_view(request, disciplina_id):
    curso = Disciplina.objects.get(id=disciplina_id)
    curso.delete()
    return redirect('cursos:index')

