from wsgiref.validate import validator

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from core.managers import BaseManager,StudentManager

class Lecturer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'lecturers'
        verbose_name = 'lecturer'
        verbose_name_plural = 'lecturers'

class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    lecturer = models.ForeignKey(Lecturer, on_delete= models.SET_NULL, null=True, related_name='courses')
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    duration = models.IntegerField(null=True)
    objects = BaseManager()


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'courses'
        verbose_name = 'course'
        verbose_name_plural = 'courses'

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True, null=True)
    grade = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        null=True,
        blank=True,
    )
    courses = models.ManyToManyField(Course, related_name='students')
    is_active = models.BooleanField(default=True)
    objects = StudentManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
