from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField(verbose_name='Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def  __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(verbose_name='Content')
    comments = models.ManyToManyField(Comment)
    def  __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'