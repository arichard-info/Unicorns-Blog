from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  

class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='image', verbose_name='Image')
    def  __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


 
class Comment(models.Model):
    content = models.TextField(verbose_name='Content')
    author = models.CharField(max_length=200)
    approved_comment = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    def approve(self):
        self.approved_comment = True
        self.save()
    def  __str__(self):
        return self.content
    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'