# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Student(User):
    uovog = models.CharField(max_length = 40,verbose_name ='Ургийн овог')
    regNumber = models.CharField(max_length = 10, verbose_name='Регистрийн дугаар')
    ynemNumber = models.CharField(max_length = 9,verbose_name='Иргэний үнэмлэхний дугаар')
    address = models.CharField(max_length = 150, verbose_name='Гэрийн хаяг')
    phone = models.IntegerField(verbose_name='Утасны дугаар')
    
class Teacher(User):
    erdem_zereg = models.CharField(max_length = 20)
        
class NarBichig(User): 
    name = models.CharField(max_length = 20)
    
class NewsType(models.Model):
    typename  = models.CharField(max_length = 20)
    
class News(models.Model):
    code = models.CharField(max_length = 10)
    newstype  = models.ForeignKey(NewsType)
    content = models.TextField()
    NBName = models.CharField(max_length = 20)
    date = models.DateField()
    
class Uzleg(models.Model):
    name = models.CharField(max_length = 50)
    date = models.DateField()
    time = models.TimeField()
    commis = models.CharField(max_length = 50)
    room = models.IntegerField()
    shaardlaga = models.TextField()

class score(models.Model):
    uzleg  = models.ForeignKey(Uzleg)
    student = models.ForeignKey(Student)
    score = models.IntegerField()
        
class SedevInfo(models.Model):
    name = models.CharField(max_length = 20,verbose_name='Сэдвийн нэр')
    english_name = models.CharField(max_length = 30,verbose_name='Сэдвийн англи нэр')
    shaardlaga = models.TextField(verbose_name='Шаардлага')
    
    def __unicode__(self):
        return self.name
    
class songoson_sedev(models.Model):
    sedev = models.ForeignKey(SedevInfo)
    tugsult_code = models.IntegerField()
    date = models.DateField()
    stu_year = models.CharField(max_length = 9)
    teacher = models.ForeignKey(Teacher)
    student = models.ForeignKey(Student)   

class tugsult_ajil(models.Model):
    code = models.IntegerField()
    sedev = models.ForeignKey(SedevInfo)
    student = models.ForeignKey(Student)
    teacher = models.ForeignKey(Teacher)
    date = models.DateField()
    score = models.IntegerField()
    
class ansQue(models.Model):
    question = models.TextField()
    answer = models.TextField(null=True)
    date = models.DateField()
    user = models.ForeignKey(Student)

class IP(models.Model):
    ip = models.CharField(max_length = 20)
    port = models.IntegerField()
    key = models.CharField(max_length = 100)
