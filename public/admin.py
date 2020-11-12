from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'category', 'title', 'photo', 'content', 'created_on')
    list_filter = ('author', 'category', 'created_on')
    search_fields = ['title', 'content']


@admin.register(Category)
class ACategory(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Comment)
class AComment(admin.ModelAdmin):
    list_display = ('post', 'name', 'body', 'created_on')
    list_filter = ('post', 'created_on')
    search_fields = ['name', 'body']
