
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Post, Tag
from users.models import Profile
from .forms import PostForm

def posts(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request,"posts/posts.html",context)


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



def post_create(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.owner = request.user.profile
            post.save()
            return redirect("posts")

    context = {"form":form}
    return render(request,"posts/posts.html",context)