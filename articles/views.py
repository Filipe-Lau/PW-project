from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


def index_view(request):
    context = {
        'articles': Article.objects.all().order_by('title'),
    }

    return render(request,'articles/index.html',context)


def article_view(request, article_id):
    context = {
        'article': Article.objects.get(id=article_id),
    }

    return render(request,'articles/article.html',context)

@login_required
def new_article_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('articles:index')

    context = {'form': form}
    return render(request, 'articles/new_article.html', context)


@login_required
def edit_article_view(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.POST:
        form = ArticleForm(request.POST or None, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article':article}
    return render(request, 'articles/edit_article.html', context)


@login_required
def delete_article_view(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles:index')