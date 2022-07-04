from urllib import response
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Profile, Message, Chat
from .forms import AccountForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def profile(request, pk):
    profile = Profile.objects.get(id = pk)
    posts = profile.owner.all()

    context = {"profile":profile,"posts":posts}
    return render(request,"users/profile.html", context)


@login_required(login_url="login")
def account(request,pk):
    
    profile = Profile.objects.get(id = pk)
    posts = profile.owner.all()
    form = AccountForm(instance=profile)
    

    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            return redirect("account", pk=request.user.profile.id)

    context = {"profile":profile,"form":form, "posts":posts}
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


def user_chats(request, pk):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    profiles = Profile.objects.filter(Q(name__icontains = search_query))
    
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
    context = {"chats":chats,"profiles":profiles}
    return render(request, "users/user_chats.html", context)


def user_chat(request,pk):
    chat = Chat.objects.get(id=pk)
    chat_messages = chat.message_set.all()
    
    context = {"chat":chat, "chat_messages":chat_messages}
    return render(request, "users/user_chat.html", context)

def create_chat(request, pk):
    profile = Profile.objects.get(id=pk)
    chat = Chat.objects.create(
        chat_member_one = request.user.profile,
        chat_member_two = profile
    )
    chat.save()
    return redirect("user_chat", pk=chat.id)