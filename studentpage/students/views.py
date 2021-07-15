from django.shortcuts import render , redirect
from.models import *
from django.http import HttpResponse
from django.views.generic import View 
from .utils import *
from .forms import certInquiryForm
from django.contrib import messages

# Create your views here.


def home(request):
  students= Student.objects.all()
  courses = Course.objects.all()
  return render(request,'index.html',locals())



def cert(request):
  if request.method == 'POST':
    inquiry_form  = certInquiryForm(request.POST, request.FILES)
    if inquiry_form.is_valid():
          inquiry_form.save()
          messages.success(request,f'Your message has been received')
          messages.success(request,f'Your Profile account has been updated successfully')

          inquiry_form.save()
          return redirect ('/')
      
  else:
    inquiry_form = certInquiryForm(request.POST)
      
  return render(request,'certy.html',locals())
  
class GeneratePdf(View):

  def get(self,request, *args, **kwargs):
    data = {
      'today': ' Cooper Mann',
      'certificate_id' :123456, 
    }
    pdf =render_to_pdf('pdf/certificate.html', data)
    return HttpResponse(pdf,content_type = 'application/pdf')

  

def stats(request):
  students = Student.objects.all()
  courses = Course.objects.all()
  x = [ x.name for x in students]
  y = [y.title for y in courses]
  chart = get_plot(x,y)
  return render(request,'stats.html', {'chart': chart})