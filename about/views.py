from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()  

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(request, "Collaboration request received! I endeavour to respond within 2 working days.")
            return redirect('about') 
    else:
        collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )

def submit_collaborate_request(request):
    if request.method == 'POST':
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(request, 'Collaboration request received! I endeavour to respond within 2 working days.')
            return redirect('about')
        else:
            messages.error(request, 'Collaboration request form is not valid!')
    return render(request, 'about/about.html', {'collaborate_form': CollaborateForm()})