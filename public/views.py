from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignForm, AddForm, ComForm
from .models import Post, Category
from blog.models import Post as Pt

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        form = SignForm(request.POST)

        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('uhome')

    else:
        form = SignForm(request.POST)

    posts = Pt.objects.filter(status=1).order_by('-created_on')
    return render(request, 'users/signup.html', {'form': form,
                                                 'posts': posts,
                                                 })


def log_in(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('uhome')

    posts = Pt.objects.filter(status=1).order_by('-created_on')
    return render(request, 'users/log_in.html', {'posts': posts})


def uhome(request):
    user = request.user
    posts = Post.objects.filter(author=user).order_by('-created_on')
    return render(request, 'users/home.html', {'posts': posts})


def add_post(request):
    user = request.user

    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('uhome')

    cat = Category.objects.all()
    form = AddForm()
    return render(request, 'users/add.html', {'form': form,
                                              'cate': cat,
                                              })


def explore(request):
    posts = Post.objects.order_by('-created_on')
    return render(request, 'users/home.html', {'posts': posts})


def post_detail(request, title):
    user = request.user
    post = get_object_or_404(Post, title=title)

    if request.method == "POST":
        form = ComForm(request.POST)

        if form.is_valid():
            com = form.save(commit=False)
            com.post = post
            com.name = user
            com.save()
            return redirect('uhome')

    comments = post.comments.all()
    form = ComForm()
    return render(request, 'users/detail.html', {'post': post,
                                                 'form': form,
                                                 'coms': comments,
                                                 })


def pro_view(request, author):
    posts = Post.objects.filter(author=author).order_by('-created-on')

    return render(request, 'users/pro.html', {'posts': posts})


def log_out(request):
    logout(request)
    return redirect('home')
