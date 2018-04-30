from django.test import TestCase
from django.urls import reverse
from django.db.models.query import QuerySet
from blog.models import Article, Comment

# Create your tests here.

class WebsiteTestCase(TestCase):
    fixtures = ['initial.json', ]
    def test_index_page(self):
        response = self.client.get(reverse('blog:index'))
        articles = [article.__repr__() for article in Article.objects.all().order_by('-release_date')[:6]]
        self.assertQuerysetEqual(response.context['articles'], articles)
        self.assertTemplateUsed('partials/index.html')
        self.failUnlessEqual(response.status_code, 200)
        

        
    def test_article_page(self):
        article = Article.objects.first()
        response = self.client.get(reverse('blog:article', kwargs={'slug': article.slug}))
        self.assertContains(response, article.title)
        self.assertEqual(type(response.context['article']), Article)
        self.assertEqual(type(response.context['comments'][1]), Comment)
        self.assertEqual(response.context['last_articles'].count(), 3)
        self.assertTemplateUsed('partials/single_article.html')
        self.failUnlessEqual(response.status_code, 200)
        


    def test_about_page(self):
        response = self.client.get(reverse('blog:about'))
        self.assertTemplateUsed('partials/about.html')
        self.failUnlessEqual(response.status_code, 200)
        


    def test_search_page(self):
        response = self.client.get(reverse('blog:search'))
        self.assertTemplateUsed('partials/search.html')
        self.assertEqual(type(response.context['items'][1]), Article)
        self.failUnlessEqual(response.status_code, 200)
        
