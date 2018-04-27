from django.test import TestCase
from django.urls import reverse
from django.db.models.query import QuerySet
from blog.models import Article

# Create your tests here.

class WebsiteTestCase(TestCase):
    fixtures = ['initial.json', ]
    def test_index_page(self):
        response = self.client.get(reverse('blog:index'))
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')

        
    def test_post_page(self):
        # Published news
        article = Article.objects.first()
        response = self.client.get(reverse('blog:article', kwargs={'slug': article.slug}))
        self.assertContains(response, article.title)
        self.assertEqual(type(response.context['article']), Article)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed('article.html')
