from django.db import models
from django.utils import timezone

# Create your models here.



class Course(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=1890, null=True)
    date_posted =models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.title


    @classmethod
    def all_courses(cls):
        courses = cls.objects.all()
        return courses



class Student(models.Model):
    name = models.CharField(max_length=89)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    @classmethod
    def all_students(cls):
        students = cls.objects.all()
        return students

