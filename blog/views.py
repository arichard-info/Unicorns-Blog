from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()[:3]
    return render(request, 'partials/index.html', {'latests_articles': articles})

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('/article/' + slug)
    else:
        form = CommentForm()
    return render(request, 'partials/single_article.html', {'article': article, 'form' : form})


def about(request):
    return render(request, 'partials/about.html', {})

def contact(request):
    return render(request, 'partials/contact.html', {})