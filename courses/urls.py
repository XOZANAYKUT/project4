from django.urls import path
from . import views

urlpatterns = [  
    path('search/', views.search_results, name='search_results'),   
    path('<slug:slug>/', views.course_detail, name='course_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('', views.CourseList.as_view(), name='home'),
]