from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    content = models.CharField(max_length=350)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def  __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

class Article(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=500)
    comments = models.ManyToManyField(Comment)
    def  __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'