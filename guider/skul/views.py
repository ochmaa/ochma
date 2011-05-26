# -*- coding: utf-8 -*- 
from django.template import RequestContext
from django.template import Context, loader
from django.views.generic import simple
from django.shortcuts import render_to_response
import urllib
from skul.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
import datetime
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
import django.core.files
from django.views.generic import create_update
from forms import *
from django.template import RequestContext
def root_view(request):
    return render_to_response('home.html',context_instance=RequestContext(request))

def student_register(request):
    return create_update.create_object(
        request,
        form_class = StudentRegForm,
        post_save_redirect = reverse('home-student'),
        template_name = 'student/studentregister.html'
    )


def teacher_addtopic(request):
    return create_update.create_object(
        request,
        form_class = SedevInfoForm,
        post_save_redirect = reverse('home-teacher'),
        template_name = 'teacher/TeacherSedevAdd.html'
    )


def teacher_adduzleg(request):
    return create_update.create_object(
        request,
        model = Uzleg,
        post_save_redirect = reverse('home-teacher'),
        template_name = 'teacher/adduzleg.html'
    )

def student_home(request):
    return render_to_response('student/studentHome.html')

def nabi_home(request):
    return render_to_response('NaBi/NaHome.html')

def nabi_student(request):
    if request.method == "GET":
        student = Student.objects.all()
        t = loader.get_template('NaBi/NaStudent.html')
        c = Context({
        'student': student,
        })
        return HttpResponse(t.render(c))


def nabi_teacher(request):
    return create_update.create_object(
        request,
        form_class = NabiTeacherForm,
        post_save_redirect = reverse('teacher-nabi'),
        template_name = 'NaBi/NaTeacher.html',
        extra_context = {
            'object_list': Teacher.objects.all()
        }
    )

def nabi_uzleg(request):
    return create_update.create_object(
        request,
        form_class = NabiUzlegForm,
        post_save_redirect = reverse('uzleg-nabi'),
        template_name = 'NaBi/NaYzleg.html',
        extra_context = {
            'object_list': Uzleg.objects.all()
        }
    )

def nabi_send(request):
    return render_to_response('NaBi/NaNewsSend.html')

def nabi_zar(request):
    return create_update.create_object(
        request,
        form_class = NaZarForm,
        post_save_redirect = reverse('zar-nabi'),
        template_name = 'NaBi/NaZar.html',
        extra_context = {
            'object_list': News.objects.all()
        }
    )

def ex_home(request):
    return render_to_response('material.html')

def teacher_home(request):
    return render_to_response('teacher/TeacherHome.html')

def teacher_news(request):
    return render_to_response('teacher/TeacherNews.html')


@login_required()
def FAQ_home(request):
    if request.method == "GET":
        aq = ansQue.objects.all()[:10]
        t = loader.get_template('FAQ.html')
        c = Context({
        'aq':aq,
        })
        return HttpResponse(t.render(c))
    else:
        question = request.POST['question']
        user = request.user
        ansQue.objects.create(
            question = question,
            answer = '1',
            date = datetime.datetime.now(),
            user = user)
    return HttpResponseRedirect(reverse('home-FAQ'))

def contact(request):
    return render_to_response('contact.html')

def stuSedev(request):
    return render_to_response('student/studentSedev.html')

def student_login(request):
    username = request.POST['name']
    password = request.POST['code']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('student/studentHome.html')
        else:
            return render_to_response('student/studentHome.html')
    else:
        return render_to_response('home.html')

@login_required()
def student_score(request):
    return render_to_response('student/studentYzlegScore.html')

@login_required()
def student_sedev(request):
    return create_update.create_object(
        request,
        model = songoson_sedev,
        post_save_redirect = reverse('home-student'),
        template_name = 'student/studentSedev.html'
    )
 


@login_required()
def student_yzhuv(request):
    if request.method == "GET":
        uzlegs = Uzleg.objects.all()
        nowyz  = Uzleg.objects.filter(date__gt = datetime.now())
        t = loader.get_template('student/studentYzleg.html')
        c = Context({
        'uzlegs': uzlegs,
        'nowyz': nowyz,
        })
        return HttpResponse(t.render(c))


def teacher_student(request):
    return render_to_response('teacher/TeacherStudent.html')  

def contact_message(request):
    if request.method == "GET":
        return render_to_response('student/studentregister.html')
    else:
        name=request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        garchig = 'Холбогдох хүсэлт'
        to = 'ochma_lucky@yahoo.com'
        send_mail(garchig, message, email, [to], fail_silently=False)
    return render_to_response('home.html')

def sendsms(phone,content):
    ip = IP.objects.all()[0]
    urllib.urlopen('http://%s:%s/send?to=%s&content=%s'%(ip.ip,ip.port,phone,content))    
