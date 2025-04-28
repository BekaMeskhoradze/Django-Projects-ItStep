from django.db import models

class Lecturers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True, null=True)

    class Meta:
        db_table = 'lecturers'

class Courses(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    lecturer = models.ForeignKey(Lecturers, on_delete= models.SET_NULL, null=True)

    class Meta:
        db_table = 'courses'

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True, null=True)
    grade = models.IntegerField()
    courses = models.ManyToManyField(Courses)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'students'
