from django.shortcuts import render
from django.db.models import Q
from .models import Post, Tag
from users.models import Profile

def posts(request):
    return render(request,"posts/posts.html")


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
    posts = tag.post #TODO spraviť to tak aby sa vypisali projekty z tymto tagom kôli searchu
    context = {"posts":posts}
    return render(request,"posts/tag_view.html", context)