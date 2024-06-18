from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Course, Comment
from .forms import CommentForm, CourseForm


class CourseList(generic.ListView):
    queryset = Course.objects.filter(status=1)
    template_name = "courses/index.html"
    paginate_by = 6


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if not request.user.is_authenticated:
        messages.error(request, 'You need to log in to edit comments.')
        return redirect('account_login')

    queryset = Course.objects.filter(status=1)
    course = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment_form = CommentForm(data=request.POST, instance=comment)

    if comment.author != request.user:
        messages.add_message(request, messages.ERROR, 'You can only edit your own comments!')
        return HttpResponseRedirect(reverse('course_detail', args=[slug]))

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
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
    View to delete comment
    """

    if not request.user.is_authenticated:
        messages.error(request, 'You need to log in to delete comments.')
        return redirect('account_login')

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
    """
    View function for displaying search results based on user query.

    Retrieves the search query entered by the user from the request.
    Validates the search query and displays appropriate error messages if invalid.
    Performs a search on course titles and content containing the query.
    Returns a list of courses matching the search query to be displayed.

    *Context*
    ''courses''
        An instance of :model:course.Course

    *Template*
    courses/search_results.html
    """
    query = request.GET.get('q')

    if not query:
        messages.add_message(request, messages.ERROR, "Please enter a search query.")
        return render(request, 'courses/search_results.html', {'courses': []})

    if len(query) > 100:
        messages.add_message(request, messages.ERROR, "Search query is too long. Maximum length is 100 characters.")
        return render(request, 'courses/search_results.html', {'courses': []})

    courses = Course.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'courses/search_results.html', {'courses': courses})


def add_course(request):
    """ Add a course to the website """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can add courses.')
        return redirect(reverse('account_login'))

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Successfully added course!')
            return redirect(reverse('course_detail', args=[course.slug]))
        else:
            messages.error(request, 'Failed to add course. Please ensure the form is valid.')
    else:
        form = CourseForm()

    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_course(request, slug):
    """ Edit a course on the website """
    course = get_object_or_404(Course, slug=slug)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can edit courses.')
        return redirect(reverse('course_detail', args=[course.slug]))

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated course!')
            return redirect(reverse('course_detail', args=[course.slug]))
        else:
            messages.error(request, 'Failed to update course. Please ensure the form is valid.')
    else:
        form = CourseForm(instance=course)
    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)


def delete_course(request, slug):
    """ Delete a course from the website """

    course = get_object_or_404(Course, slug=slug)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can delete courses.')
        return redirect(reverse('course_detail', args=[course.slug]))

    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Successfully deleted course!')
        return redirect(reverse('home'))
    template = 'courses/delete_course.html'
    context = {
        'course': course,
    }

    return render(request, template, context)