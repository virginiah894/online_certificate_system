from django import forms
from .models import Student , Course, Grade
from crispy_forms.helper import FormHelper
from  crispy_forms.layout import Submit,Layout,Field






class certInquiryForm(forms.ModelForm):
    class Meta:
        model = Student
        fields  = ['name', 'email','course','image' ,'grade']