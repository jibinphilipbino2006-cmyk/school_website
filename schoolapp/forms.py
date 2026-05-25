from django import forms
from .models import *


class ClassForm(forms.ModelForm):

    class Meta:
        model = ClassRoom
        fields = ['class_name']


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['name']


class DivisionForm(forms.ModelForm):

    class Meta:
        model = Division
        fields = [
            'classroom',
            'division_name',
            'class_teacher'
        ]


class TeacherForm(forms.ModelForm):

    class Meta:

        model = Teacher

        fields = [
            'name',
            'email',
            'phone_no'
        ]
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'name',
            'roll_no',
            'phone_no',
            'email',
            'division'
        ]