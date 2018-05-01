from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='image', verbose_name='Image')
    def  __str__(self):
        return self.title
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


 
class Comment(models.Model):
    content = models.TextField(verbose_name='Contenu')
    author = models.CharField(max_length=200, verbose_name='Pseudo')
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