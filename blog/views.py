from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Blog
from django.views.generic.edit import CreateView


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'all_blog'

    def get_queryset(self):
        return Blog.objects.all()

class DetailView(generic.DetailView):
    model= Blog
    template_name = 'blog/detail.html'

class BlogCreate(CreateView):
    model = Blog
    fields = ['blog_title','sub_title','body']
