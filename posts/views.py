
import re
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Post, Tag
from users.models import Profile
from .forms import PostForm
from django.contrib import messages

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


def post_comments(request, pk):
    post = Post.objects.get(id=pk) 
    context = {"post":post }
    return render(request,"posts/post_comments.html", context)


