from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
    path('submit_collaborate_request/', views.submit_collaborate_request, name='submit_collaborate_request'),  #
]