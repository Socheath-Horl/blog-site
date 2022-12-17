from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset() \
                        .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)   # the date will be saved automatically when creating an object
    updated = models.DateTimeField(auto_now=True)       # the date will be updated automatically when saving an object
    status = models.CharField(
        max_length=2, 
        choices=Status.choices,
        default=Status.DRAFT
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog:post_detail', 
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )
