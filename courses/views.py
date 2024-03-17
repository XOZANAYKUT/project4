from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from .models import Course, Comment
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import CommentForm

class CourseList(generic.ListView):
    queryset = Course.objects.filter(status=1)
    template_name = "courses/index.html"
    paginate_by = 6

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Course.objects.filter(status=1)
        course = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.course = course
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('course_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Course.objects.filter(status=1)
    course = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('course_detail', args=[slug]))    

def course_detail(request, slug):
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
            return redirect('course_detail', slug=slug)

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
    
def search_results(request):
    query = request.GET.get('q')
    courses = Course.objects.filter(title__icontains=query)
    return render(request, 'courses/search_results.html', {'courses': courses})