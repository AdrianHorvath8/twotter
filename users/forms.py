from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ["first_name", "email", "username", "password1", "password2"]:
            self.fields[fieldname].help_text = None


class AccountForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user","username","followers","post","following"]

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["body","message_image"]