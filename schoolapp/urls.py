from django.urls import path
from . import views


urlpatterns = [

    # Home Page
    path(
        '',
        views.home,
        name='home'
    ),

    # Admin Dashboard
    path(
        'admin-page/',
        views.admin_page,
        name='admin_page'
    ),

    # Class Page
    path(
        'class/<int:division_id>/',
        views.class_page,
        name='class_page'
    ),

    # Edit Student
    path(
        'edit-student/<int:student_id>/',
        views.edit_student,
        name='edit_student'
    ),

    # Delete Student
    path(
        'delete-student/<int:student_id>/',
        views.delete_student,
        name='delete_student'
    ),

    # Delete Class
    path(
        'delete-class/<int:id>/',
        views.delete_class,
        name='delete_class'
    ),

    # Delete Division
    path(
        'delete-division/<int:id>/',
        views.delete_division,
        name='delete_division'
    ),
    path(
    'edit-division/<int:id>/',
    views.edit_division,
    name='edit_division'
    ),
    path(
    'delete-class/<int:id>/',
    views.delete_class,
    name='delete_class'
    ),
]