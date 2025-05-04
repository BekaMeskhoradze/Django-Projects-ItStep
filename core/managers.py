from django.db import models

class BaseManager(models.Manager):
    def get_expensive_courses(self):
        return self.get_queryset().filter(price__gt=1600)

class StudentManager(models.Manager):
    def active_students(self):
        return self.get_queryset().filter(is_active=True)

    def inactive_students(self):
        return self.get_queryset().filter(is_active=False)

    def adult_students(self):
        return self.get_queryset().filter(age__gte=20)