from django import forms
from .models import Comment, Course

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SearchForm(forms.Form):
    query = forms.CharField(label='Search')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'slug', 'author', 'featured_image', 'content', 'date', 'duration', 'status', 'excerpt']