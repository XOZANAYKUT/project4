from django.shortcuts import render
from django.http import HttpResponse
from .models import About

def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )

def submit_form(request):
    """
    Handles form submission
    """
    if request.method == 'POST':
        # Form verilerini işleme kodları buraya gelecek
        return HttpResponse('Form submitted successfully!')
    else:
        return HttpResponse('This URL only accepts POST requests.')