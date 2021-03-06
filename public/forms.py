from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class SignForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AddForm(forms.ModelForm):
    category = forms.Select()

    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'category']


class ComForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
