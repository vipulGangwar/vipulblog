from django.conf.urls import url
from . import views
from django.views.generic import ListView,DetailView

app_name='blog'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^blog/(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    url(r'blog/blog/add/$',views.BlogCreate.as_view(), name='blog_add'),
]