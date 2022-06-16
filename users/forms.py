from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]


class AccountForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user","followers","post"]