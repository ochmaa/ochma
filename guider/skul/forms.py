# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import Student, SedevInfo
from django.forms.extras import widgets

class StudentRegForm(UserCreationForm):	
    class Meta:
        model = Student
        fields = ('username', 'first_name','last_name','email','uovog','regNumber','address','phone')

class SedevInfoForm(forms.ModelForm):
    name = forms.CharField( label='Сэдвийн нэр',error_messages= {
        'required': 'Сэдвийн нэрээ оруулна уу'
    })
    english_name = forms.CharField( label='Сэдвийн англи нэр',error_messages = {
        'required': 'Сэдвийн англи нэрийг оруулна уу'
    })
    class Meta:
        model = SedevInfo
        fields = ('name','english_name','shaardlaga') 
