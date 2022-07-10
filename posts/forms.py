
from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["body","post_image"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields["body"].widget.attrs.update({"placeholder":"What's happening?"})



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body","comment_image"]