# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import Student, SedevInfo
from django.forms.extras import widgets

class StudentRegForm(UserCreationForm):	
    username = forms.CharField( label='Оюутны код',error_messages= {
        'required': 'Кодоо оруулна уу?'
    })
    first_name = forms.CharField( label='Овог',error_messages= {
        'required': 'Овогоо оруулна уу?'
    })
    last_name = forms.CharField( label='Нэр',error_messages= {
        'required': 'Нэрээ оруулна уу?'
    })
    email = forms.CharField( label='Цахим хаяг',error_messages= {
        'required': 'Цахим хаягаа оруулна уу?'
    })
    uovog = forms.CharField( label='Ургийн овог',error_messages= {
        'required': 'Ургын овгоо оруулна уу?'
    })
    regNumber = forms.CharField( label='Регистрийн дугаар',error_messages= {
        'required': 'Регистрийн дугаараа оруулна уу?'
    })
    phone = forms.CharField( label='Утасны дугаар',error_messages= {
        'required': 'Утасны дугаараа оруулна уу?'
    })

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

class NabiTeacher(forms.ModelForm):
    class Meta:
	model = Teacher
        fields = ('username','first_name','last_name', 'email', 'erdem_zereg') 
	
