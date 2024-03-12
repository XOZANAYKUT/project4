from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Course
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

    return render(
        request,
        "courses/course_detail.html",
        {"course": course},
    )