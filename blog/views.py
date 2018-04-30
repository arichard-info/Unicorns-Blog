from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import CommentForm
from blog.models import Article, Comment




# Create your views here.
def index(request):
    articles_list = Article.objects.all().order_by('-release_date')
    paginator = Paginator(articles_list, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'partials/index.html', {'articles': articles})



def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    last_articles = Article.objects.order_by('-release_date')[0:3]
    comments = Comment.objects.filter(article=article).order_by('-created_date')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('/article/' + slug)
    else:
        form = CommentForm()
        
    return render(
        request, 
        'partials/single_article.html', 
        {
            'article': article, 
            'comments': comments,
            'form' : form, 
            'last_articles' : last_articles
        }
    )



def search(request):
    template = 'partials/search.html'
    query = request.GET.get('q')
    if query:
        results = Article.objects.filter(Q(title__icontains = query) | Q(content__icontains = query))
    else:
        results = Article.objects.all()

    nb_results = results.count()
        
    context = {
        'items' : results,
        'nb_results' : nb_results,
        'query_search' : query,
    }

    return render(request, template, context)




def about(request):
    return render(request, 'partials/about.html', {})



