from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from datetime import date

from .models import BlogPost
from .forms import BlogPostForm

# Verifica se o user que criou o tópico é o user logado.


def logado(owner, user_log):
    if owner != user_log:
        raise Http404

# Create your views here.


def index(request):
    posts = BlogPost.objects.filter(
        date_added__gte=date(2021, 1, 16)
    ).order_by('-date_added')  # pode se usar: [:3]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


@login_required
def posts(request):
    posts = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blog/posts.html', context)


def post(request, post_id):
    posts = BlogPost.objects.get(id=post_id)
    context = {'posts': posts}
    return render(request, 'blog/post.html', context)


@login_required
def new_post(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blog:posts')

    context = {'form': form}
    return render(request, 'blog/new_post.html', context)


@login_required
def edit_post(request, post_id):
    posts = BlogPost.objects.get(id=post_id)
    logado(posts.owner, request.user)

    if request.method != 'POST':
        form = BlogPostForm(instance=posts)
    else:
        form = BlogPostForm(instance=posts, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post', post_id=posts.id)

    context = {'posts': posts, 'form': form}
    return render(request, 'blog/edit_post.html', context)


@login_required
def del_post(request, post_id):
    posts = BlogPost.objects.get(id=post_id)
    logado(posts.owner, request.user)

    if request.method != 'POST':
        context = {'posts': posts}
        return render(request, 'blog/del_post.html', context)
    else:
        posts.delete()
        return redirect('blog:posts')
