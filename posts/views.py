
import re
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Post, Comment
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

    if request.user.profile == post.owner:
        pass
    else:
        return redirect("posts")

    if request.method=="POST":
        post.delete()
        messages.success(request, "Post was delete successfuly")
        return redirect(request.GET["next"] if "next" in request.GET else "posts") 

    
    return render(request,"delete_template.html")


def search(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    profiles = Profile.objects.filter(Q(name__icontains = search_query))
    posts = Post.objects.filter(Q(body__icontains = search_query))


    context = {"profiles":profiles, "search_query":search_query,"posts":posts}
    return render(request,"posts/search.html", context)




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


@login_required(login_url="login")
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)


    if request.user.profile == comment.comentator:
        pass
    else:
        return redirect("posts")

    if request.method=="POST":
        comment.delete()
        messages.success(request, "Comment was delete successfuly")
        return redirect(request.GET["next"] if "next" in request.GET else "posts")
    return render(request,"delete_template.html")


@login_required(login_url="login")
def post_like(request,pk):
    post = Post.objects.get(id = pk)
    post.like.add(request.user.profile)
    
    return redirect(request.GET["next"] if "next" in request.GET else "posts")


@login_required(login_url="login")
def post_remove_like(request, pk):
    post = Post.objects.get(id = pk)
    post.like.remove(request.user.profile)
    
    return redirect(request.GET["next"] if "next" in request.GET else "posts")


@login_required(login_url="login")
def comment_like(request,pk):
    comment = Comment.objects.get(id = pk)
    comment.like.add(request.user.profile)
    
    return redirect(request.GET["next"] if "next" in request.GET else "posts")


@login_required(login_url="login")
def comment_remove_like(request, pk):
    comment = Comment.objects.get(id = pk)
    comment.like.remove(request.user.profile)
    
    return redirect(request.GET["next"] if "next" in request.GET else "posts")