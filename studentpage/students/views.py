from django.shortcuts import render , redirect
from.models import *

# Create your views here.


def home(request):
  students= Student.objects.all()
  courses = Course.objects.all()
  return render(request,'index.html',{'students':students},{'courses':courses})

