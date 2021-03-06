from __future__ import unicode_literals

from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class PostManager(models.Manager):
    def all(self):
        return super(PostManager, self).filter(publish=True)


class Category(models.Model):
    title = models.CharField(max_length=65)
    # slug = models.SlugField(unique=True)
    description = models.TextField(max_length=155)

    def __unicode__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('category', args=[str(self.slug)])

class Post(models.Model):
    publish = models.BooleanField(default=False)
    author = models.ForeignKey(User, null=True, blank=True)
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=65)
    # slug = models.SlugField(unique=True)
    description = models.TextField(max_length=155)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['-published_date',]\

    def __unicode__(self):
        return self.title

    def get_previous_post(self):
        return self.get_previous_published_date()

    def get_next_post(self):
        return self.get_next_published_date()

    objects = PostManager()