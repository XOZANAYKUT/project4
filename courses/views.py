from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Course
from django.contrib import messages
from .forms import CommentForm
# Create your views here.

class CourseList(generic.ListView):
    queryset = Course.objects.filter(status=1)
    template_name = "courses/index.html"
    paginate_by = 6

def course_detail(request, slug):
    """
    Display an individual :model:courses.Course.

    *Context*

    `course`
        An instance of :model:courses.Course.

    *Template:*

    :template:courses/course_detail.html
    """

    
    queryset = Course.objects.filter(status=1)
    course = get_object_or_404(queryset, slug=slug)
    comments = course.comments.all().order_by("-created_on")
    comment_count = course.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.course = course
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')
            return redirect('course_detail', slug=slug)  # Burada sayfayı tekrar yükleyerek formun temizlenmesini sağlıyoruz.

    return render(
        request,
        "courses/course_detail.html",
        {
            "course": course,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )