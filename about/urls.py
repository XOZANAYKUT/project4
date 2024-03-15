from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
    path('submit_form/', views.submit_form, name='submit_form'), 
]