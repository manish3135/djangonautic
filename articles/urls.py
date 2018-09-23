from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$',views.articles_list, name="list"),
    url(r'^article_create/$',views.article_create, name="Create"),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name="detail"),
]
