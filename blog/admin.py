from django.contrib import admin
from .models import Post, Comment, Category, AField

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'category', 'image', 'status', 'created_on')
    list_filter = ('author', 'status', 'created_on')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'created_on')
    list_filter = ('post',)
    search_fields = ['name', 'body']


@admin.register(AField)
class AFieldAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'file')
    list_filter = ('name',)


@admin.register(Category)
class ACategory(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    list_filter = ('created_on',)
