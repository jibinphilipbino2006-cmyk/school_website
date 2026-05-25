from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError

# Teacher Model
class Teacher(models.Model):

    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                4,
                message='Teacher name must contain at least 4 letters.'
            )
        ]
    )

    email = models.EmailField()

    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# Class Model
class ClassRoom(models.Model):

    class_name = models.CharField(
        max_length=50,
        unique=True,
        validators=[
           MinLengthValidator(
                4,
                message='Class must contain exactly 3 digits.'
            )
        ]
    )

    def __str__(self):
        return self.class_name


# Division Model

class Division(models.Model):

    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )

    division_name = models.CharField(max_length=20)

    class_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = (
            'classroom',
            'division_name'
        )

    def clean(self):

        # Check if teacher already assigned to another class
        if self.class_teacher:

            existing_teacher = Division.objects.filter(
                class_teacher=self.class_teacher
            ).exclude(id=self.id)

            if existing_teacher.exists():

                raise ValidationError({
                    'class_teacher':
                    'This teacher is already assigned to another class.'
                })

    def save(self, *args, **kwargs):

        self.full_clean()   # Run validation

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.classroom.class_name} - {self.division_name}"

# Student Model
class Student(models.Model):

    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                4,
                message='Student name must contain at least 4 letters.'
            )
        ]
    )

    roll_no = models.IntegerField()

    phone_no = models.CharField(
        max_length=15,
        validators=[
                MinLengthValidator(
                10,
                message='Phone must contain at least 10 digits.'
            )
        ]
    )

    email = models.EmailField()

    division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name