
import re
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Post, Tag
from users.models import Profile
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def posts(request):
    posts = Post.objects.all()
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user.profile
            post.save()
            return redirect("posts")
    context = {"posts":posts, "form":form}
    return render(request,"posts/posts.html",context)

@login_required(login_url="login")
def delete_post(request,pk):
    post = Post.objects.get(id=pk)

    if request.method=="POST":
        post.delete()
        messages.success(request, "Post was delete successfuly")
        return redirect("account", pk = request.user.profile.id)

    context= {"obj":post}
    return render(request,"delete_template.html", context)


def search(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    profiles = Profile.objects.filter(Q(name__icontains = search_query))
    posts = Post.objects.filter(Q(body__icontains = search_query))
    tags = Tag.objects.filter(Q(name__icontains = search_query))

    context = {"profiles":profiles, "search_query":search_query,"posts":posts,"tags":tags}
    return render(request,"posts/search.html", context)


def tag_view(request,pk):
    tag = Tag.objects.get(id=pk)
    posts = tag.tag.all() 
    context = {"posts":posts }
    return render(request,"posts/tag_view.html", context)


@login_required(login_url="login")
def post_comments(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all()
    form = CommentForm()

    if request.method=="POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comentator = request.user.profile
            comment.post = post
            comment.save()
            return redirect(post_comments, pk = post.id)


    context = {"post":post,"comments":comments,"form":form }
    return render(request,"posts/post_comments.html", context)


