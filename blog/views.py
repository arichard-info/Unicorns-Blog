from django.shortcuts import render, get_object_or_404
from blog.models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.all()[:3]
    return render(request, 'index.html', {'latests_articles': articles})

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article.html', {'article': article})