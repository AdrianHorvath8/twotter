from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Profile
from .forms import AccountForm
from django.contrib.auth.decorators import login_required

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