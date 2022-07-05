from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]


class AccountForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user","username","followers","post"]

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["body","message_image"]