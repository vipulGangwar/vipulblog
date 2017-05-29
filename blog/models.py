from django.db import models
from django.core.urlresolvers import reverse

class Blog(models.Model):
    blog_title = models.CharField(max_length=500)
    sub_title = models.CharField(max_length=100)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.blog_title



