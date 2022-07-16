from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Profile, Chat
from posts.models import Post, Comment
from .forms import AccountForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def profile(request, pk):
    profile = Profile.objects.get(id = pk)
    posts = profile.owner.all()

    comments = Comment.objects.filter(comentator = profile)
    print(comments)
    

    context = {"profile":profile,"posts":posts, "comments":comments}
    return render(request,"users/profile.html", context)


@login_required(login_url="login")
def account(request,pk):
    
    posts = Post.objects.all()
    comments = Post.objects.none()
    for post in posts:
        comments = comments.union(post.comment_set.all())
    
    


    profile = Profile.objects.get(id = pk)
    user_posts = profile.owner.all()
    
    form = AccountForm(instance=profile)

    if request.user.profile == profile:
        pass
    else:
        return redirect("account", pk = request.user.profile.id)
    

    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            return redirect("account", pk=request.user.profile.id)

    context = {"profile":profile,"form":form, "user_posts":user_posts, "comments":comments}
    return render(request,"users/account.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect("posts")
        else:
            messages.error(request, "Username or password is incorrect")


    context = {}
    return render(request,"users/login_register.html", context)


def logout_user(request):
    logout(request)
    return redirect("posts")


def register(request):
    page = "register"
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid:  
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User successfuly created")
            login(request, user)
            
            return redirect("account", pk=request.user.profile.id) 


    context = {"page":page, "form":form}
    return render(request,"users/login_register.html", context)


@login_required(login_url="login")
def user_chats(request, pk):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    profiles = Profile.objects.filter(
        Q(name__icontains = search_query) |
        Q(username__icontains = search_query)
    )
    
    profile = Profile.objects.get(id=pk)
    chats= profile.chat_set.all().union(profile.chat_member_two.all())
    

    exclude_profiles=[]
    
    for chat in chats:   

        if request.user.profile == chat.chat_member_one:
            if chat.chat_member_one in exclude_profiles:
                pass
            else:
                exclude_profiles.append(chat.chat_member_two)

        if request.user.profile == chat.chat_member_two:
            if chat.chat_member_two in exclude_profiles:
                pass
            else:
                exclude_profiles.append(chat.chat_member_one)
    
    
    
    profiles = profiles.exclude(id__in=[user_profile.id for user_profile in exclude_profiles])
    profiles = profiles.order_by("?")[:5]
    context = {"chats":chats,"profiles":profiles}
    return render(request, "users/user_chats.html", context)


@login_required(login_url="login")
def user_chat(request,pk):
    chat = Chat.objects.get(id=pk)
    chat_messages = chat.message_set.all()

    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.owner = request.user.profile
            message.chat = chat
            message.save()
            return redirect("user_chat", pk=chat.id)
    
    page = request.GET.get("page")
    paginator = Paginator(chat_messages, 10)

    try:
        chat_messages = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        chat_messages = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        chat_messages = paginator.page(page)

    context = {"chat":chat, "chat_messages":chat_messages, "form":form,"paginator":paginator,}
    return render(request, "users/user_chat.html", context)


@login_required(login_url="login")
def create_chat(request, pk):
    profile = Profile.objects.get(id=pk)
    chat = Chat.objects.create(
        chat_member_one = request.user.profile,
        chat_member_two = profile
    )
    chat.save()
    return redirect("user_chat", pk=chat.id)


@login_required(login_url="login")
def following(request, pk):
    profile = Profile.objects.get(id=pk)
    request.user.profile.following.add(profile.user)
    profile.followers.add(request.user)
    return redirect(request.GET["next"] if "next" in request.GET else "posts")


@login_required(login_url="login")
def unfollowing(request, pk):
    profile = Profile.objects.get(id=pk)
    request.user.profile.following.remove(profile.user)
    profile.followers.remove(request.user)
    return redirect(request.GET["next"] if "next" in request.GET else "posts")


def followers_users(request, pk):
    profile = Profile.objects.get(id= pk)
    followers = profile.followers.all()
    followers_profiles = Profile.objects.filter(id__in=[user.profile.id for user in followers])
    
    context = {"followers_profiles":followers_profiles}
    return render(request, "users/following_followers.html", context)


def following_users(request, pk):
    profile = Profile.objects.get(id= pk)
    page = "following"
    following = profile.following.all()
    following_profiles = Profile.objects.filter(id__in=[user.profile.id for user in following])
    
    context = {"following_profiles":following_profiles, "page":page}
    return render(request, "users/following_followers.html", context)