from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def index(request):
    cat = Category.objects.all()
    recent = Post.objects.filter(status=1).order_by('-created_on')[:3]
    return render(request, 'index.html', {'recent': recent,
                                          'cat': cat,
                                          })


def blog(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    recent = Post.objects.filter(status=1).order_by('-created_on')[:3]
    cat = Category.objects.all()

    pagination = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        post_list = pagination.page(page)

    except PageNotAnInteger:
        post_list = pagination.page(1)

    except EmptyPage:
        post_list = pagination.page(pagination.num_pages)

    return render(request, 'blog/blog.html', {'posts': posts,
                                              'recent': recent,
                                              'cat': cat,
                                              'pag': pagination,
                                              'posts1': post_list,
                                              'page': page,
                                              })


def cat_view(request, name):
    cat = Category.objects.all()
    cate = get_object_or_404(Category, name=name)
    posts = cate.posts.all()
    recent = Post.objects.filter(status=1).order_by('-created_on')[:3]

    pagination = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        post_list = pagination.page(page)

    except PageNotAnInteger:
        post_list = pagination.page(1)

    except EmptyPage:
        post_list = pagination.page(pagination.num_pages)

    return render(request, 'blog/blog.html', {'posts': posts,
                                              'recent': recent,
                                              'posts1': post_list,
                                              'page': page,
                                              'pag': pagination,
                                              'cat': cat,
                                              'cate': cate,
                                              })


def blog_detail(request, title):
    post = get_object_or_404(Post, title=title)
    recent = Post.objects.filter(status=1).order_by('-created_on')[:3]
    cat = Category.objects.all()

    if request.method == "POST":
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new = form.save(commit=False)
            new.post = post
            new.save()

        return redirect('blog')

    form = CommentForm()
    comments = post.comments.order_by('-created_on')
    a_field = post.afield.all()

    return render(request, 'blog/post_detail.html', {'post': post,
                                                     'form': form,
                                                     'coms': comments,
                                                     'recent': recent,
                                                     'cat': cat,
                                                     'add': a_field,
                                                     })
