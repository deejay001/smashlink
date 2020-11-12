from django.db import models
from django.contrib.auth.models import User

# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    header = models.ImageField(upload_to='headers')
    photo = models.ImageField(upload_to='Category')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return "{} by {}".format(self.body, self.name)


class AField(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='afield')
    name = models.CharField(max_length=30, unique=True)
    file = models.FileField(upload_to='additional_fields')

    def __str__(self):
        return self.name
