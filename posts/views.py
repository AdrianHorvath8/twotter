
import pkgutil
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Post, Comment, Topic, Bookmark
from users.models import Profile
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

@login_required(login_url="login")
def posts(request):
    following = request.user.profile.following.all()
    following_profiles = Profile.objects.filter(id__in=[user.profile.id for user in following])
    posts = Post.objects.filter(Q(owner__in=[owner for owner in following_profiles]) | Q(owner = request.user.profile))
    profiles = Profile.objects.all()
    profiles = profiles.exclude(
        Q(id__in=[user_profile.id for user_profile in following_profiles]) | 
        Q(id = request.user.profile.id) 
    ).order_by("?")[:5]

    bookmarks = Bookmark.objects.filter( profile = request.user.profile)
    for bookmark in bookmarks:
        bookmark = bookmark

    page = request.GET.get("page")
    paginator = Paginator(posts, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)
    
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user.profile
            post.save()
            return redirect("posts")

    context = {"posts":posts, "form":form, "profiles":profiles, "bookmark":bookmark}
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

    profiles = Profile.objects.filter(Q(name__icontains = search_query) | Q(username__icontains = search_query))
    posts = Post.objects.filter(Q(body__icontains = search_query))
    topics = Topic.objects.filter(Q(body__icontains = search_query))[:10]
    comments = Comment.objects.filter(Q(body__icontains = search_query))


    context = {"profiles":profiles, "search_query":search_query,"posts":posts,"topics":topics,"comments":comments}
    return render(request,"posts/search.html", context)

def topic(request, pk):
    topic = Topic.objects.get(id=pk)
    posts = Post.objects.filter(body__icontains = topic.body)
    context = {"topic":topic,"posts":posts}
    return render(request,"posts/topic.html", context)




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

    
    page = request.GET.get("page")
    paginator = Paginator(comments, 5)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        comments = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        comments = paginator.page(page)


    context = {"post":post,"comments":comments,"form":form,}
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


def bookmark(request):
    bookmarks = Bookmark.objects.filter( profile = request.user.profile)
    
    for bookmark in bookmarks:
        posts = bookmark.post.all()
        bookmark = bookmark

    
    page = request.GET.get("page")
    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)
    
    context = {"bookmark":bookmark, "posts":posts}
    return render(request, "posts/bookmark.html", context)


def add_post_to_bookmark(request, pk):
    post = Post.objects.get(id=pk)
    bookmark = Bookmark.objects.filter( profile = request.user.profile)

    for i in bookmark:
        i.post.add(post)
    return redirect(request.GET["next"] if "next" in request.GET else "posts")

def remove_post_from_bookmark(request, pk):
    post = Post.objects.get(id=pk)
    bookmark = Bookmark.objects.filter( profile = request.user.profile)

    for i in bookmark:
        i.post.remove(post)
    return redirect(request.GET["next"] if "next" in request.GET else "posts")