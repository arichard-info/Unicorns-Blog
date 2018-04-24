from django.contrib import admin
from blog.models import *

# Register your models here.

"""
admin.site.register(Article)
admin.site.register(Comment)
"""


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'release_date'  )
    search_fields = ('title', )
    list_filter = ('author__username', )
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
    