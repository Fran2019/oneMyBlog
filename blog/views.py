from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

def home(request):
    return HttpResponse("hi blog reader")

def article_list(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, 'blog/article_list.html', {
        'articles': articles
    })
