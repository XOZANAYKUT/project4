from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
         model = CollaborateRequest
         fields = ('name', 'email', 'message')