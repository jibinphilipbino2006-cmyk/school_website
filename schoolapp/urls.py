from django.contrib import admin
from django.urls import path

from schoolapp import views

urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        views.home,
        name='home'
    ),

    # LOGIN PAGE
    path(
        'login/',
        views.login_page,
        name='login'
    ),

    # ADMIN PAGE
    path(
        'admin-page/',
        views.admin_page,
        name='admin_page'
    ),

    # CLASS PAGE
    path(
        'class/<int:division_id>/',
        views.class_page,
        name='class_page'
    ),

    # EDIT STUDENT
    path(
        'edit-student/<int:student_id>/',
        views.edit_student,
        name='edit_student'
    ),

    # DELETE STUDENT
    path(
        'delete-student/<int:student_id>/',
        views.delete_student,
        name='delete_student'
    ),

    # DELETE CLASS
    path(
        'delete-class/<int:id>/',
        views.delete_class,
        name='delete_class'
    ),

    # DELETE DIVISION
    path(
        'delete-division/<int:id>/',
        views.delete_division,
        name='delete_division'
    ),

    # EDIT DIVISION
    path(
        'edit-division/<int:id>/',
        views.edit_division,
        name='edit_division'
    ),

]