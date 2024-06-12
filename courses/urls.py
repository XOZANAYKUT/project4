from django.urls import path
from . import views

urlpatterns = [
    path('add_course/', views.add_course, name='add_course'),
    path('edit_course/<slug:slug>/', views.edit_course, name='edit_course'),
    path('delete_course/<slug:slug>/', views.delete_course, name='delete_course'),
    path('search/', views.search_results, name='search_results'),   
    path('<slug:slug>/', views.course_detail, name='course_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('', views.CourseList.as_view(), name='home'),
]