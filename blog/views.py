from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    return HttpResponse("hi blog reader")

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {
        'articles': articles
    })

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    return render(request, 'blog/article_detail.html', {
        'article': article
    })

