from django.db import models
from django.db.models.fields.related import OneToOneField, ForeignKey
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date


class BlogAuthor(models.Model):
    user = OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=200, help_text='Enter bio details here')

    class Meta:
        ordering = ['user', 'bio']

    def get_absolute_url(self):
        return reverse('blog-by-author', args=[str(self.id)])

    def __str__(self):
        # return f'{self.user}, {self.bio}'
        return self.user.username


class Blog(models.Model):
    name = models.CharField(max_length=500)
    author = ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=500, help_text='Enter your blog text')
    post_date = models.DateField(default=date.today())

    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class BlogComment(models.Model):
    description = models.TextField(max_length=1000, help_text='Enter comments for your blog')
    author = ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    blog = ForeignKey(Blog, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring
