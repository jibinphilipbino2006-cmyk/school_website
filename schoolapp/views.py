from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import (
    ClassForm,
    TeacherForm,
    DivisionForm,
    StudentForm
)
from django.contrib import messages
# Home Page
def home(request):

    total_students = Student.objects.count()

    total_teachers = Teacher.objects.count()

    total_classrooms = ClassRoom.objects.count()

    context = {

        'total_students': total_students,

        'total_teachers': total_teachers,

        'total_classrooms': total_classrooms,

    }

    return render(
        request,
        'home.html',
        context
    )

# Admin Page
def admin_page(request):

    classes = ClassRoom.objects.all()

    divisions = Division.objects.all()

    teachers = Teacher.objects.all()

    class_form = ClassForm()

    division_form = DivisionForm()

    teacher_form = TeacherForm()

    if request.method == 'POST':

      # Add Class
        if 'add_class' in request.POST:

            class_form = ClassForm(request.POST)

            if class_form.is_valid():

                class_form.save()
                messages.success(request, "Class added successfully!")

                return redirect('admin_page')

        # Add Division
        elif 'add_division' in request.POST:

            division_form = DivisionForm(request.POST)

            if division_form.is_valid():

                division_form.save()
                messages.success(request, "Division added successfully!")
                return redirect('admin_page')

            else:

                print(division_form.errors)

        # Add Teacher
        elif 'add_teacher' in request.POST:

            teacher_form = TeacherForm(request.POST)

            if teacher_form.is_valid():

                teacher_form.save()
                messages.success(request, "Division added successfully!")

                return redirect('admin_page')

    context = {

        'classes': classes,

        'divisions': divisions,

        'teachers': teachers,

        'class_form': class_form,

        'division_form': division_form,

        'teacher_form': teacher_form,
    }

    return render(
        request,
        'admin_page.html',
        context
    )


# Class Page
def class_page(request, division_id):

    division = get_object_or_404(
        Division,
        id=division_id
    )

    students = Student.objects.filter(
        division=division
    )

    form = StudentForm(initial={
        'division': division
    })

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'class_page',
                division_id=division.id
            )

    context = {

        'division': division,

        'students': students,

        'form': form,
    }

    return render(
        request,
        'class_page.html',
        context
    )


# Edit Student
def edit_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect(
                'class_page',
                division_id=student.division.id
            )

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        'edit_student.html',
        {
            'form': form,
            'student': student
        }
    )


# Delete Student
def delete_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    division_id = student.division.id

    student.delete()

    return redirect(
        'class_page',
        division_id=division_id
    )
from django.shortcuts import get_object_or_404, redirect


def delete_class(request, id):

    classroom = get_object_or_404(ClassRoom, id=id)

    classroom.delete()

    return redirect('admin_page')


def delete_division(request, id):

    division = get_object_or_404(Division, id=id)

    division.delete()

    return redirect('admin_page')
def edit_division(request, id):

    division = Division.objects.get(id=id)

    if request.method == 'POST':

        form = DivisionForm(request.POST, instance=division)

        if form.is_valid():

            form.save()

            return redirect('admin_page')

    else:

        form = DivisionForm(instance=division)

    return render(
        request,
        'edit_division.html',
        {'form': form}
    )
from django.shortcuts import redirect
from .models import ClassRoom


def delete_class(request, id):

    classroom = ClassRoom.objects.get(id=id)

    classroom.delete()

    return redirect('admin_page')
from django.shortcuts import render, redirect


def login_page(request):

    username = "admin"
    password = "admin123"

    if request.method == "POST":

        user = request.POST.get("username")
        pwd = request.POST.get("password")

        if user == username and pwd == password:

            return redirect('/admin-page/')

        else:

            return render(
                request,
                'login.html',
                {'error': 'Invalid Username or Password'}
            )

    return render(request, 'login.html')