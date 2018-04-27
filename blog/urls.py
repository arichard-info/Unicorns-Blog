from django.urls import path
from blog import views
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<slug:slug>', views.article, name='article'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

]