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
from forms import StudentRegForm,SedevInfoForm

def root_view(request):
    return render_to_response('home.html')

def student_register(request):
    return create_update.create_object(
        request,
        form_class = StudentRegForm,
        post_save_redirect = reverse('home-student'),
        template_name = 'studentregister.html'
    )

@permission_required('skul.add_sedev_lavlah')
def teacher_addtopic(request):
    return create_update.create_object(
        request,
        model = SedevInfo,
        post_save_redirect = reverse('home-teacher'),
        template_name = 'TeacherSedevAdd.html'
    )


def student_home(request):
    return render_to_response('studentHome.html')

def teacher_home(request):
    return render_to_response('TeacherHome.html')

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
            answer = '',
            date = datetime.datetime.now(),
            user = user)
    return HttpResponseRedirect(reverse('home-FAQ'))

def contact(request):
    return render_to_response('contact.html')

def stuSedev(request):
    return render_to_response('studentSedev.html')

def convert_utf8(value):
    if isinstance(value, unicode):
        return value.encode('utf8')
    else:
        return value

def student_login(request):
    username = request.POST['name']
    password = request.POST['code']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('studentHome.html')
        else:
            return render_to_response('studentHome.html')
    else:
        return render_to_response('home.html')

@login_required()
def student_sedev(request):
    if request.method == "GET":
        sedevs = SedevInfo.objects.all()
        t = loader.get_template('studentSedev.html')
        teachers = Teacher.objects.all()
        c = Context({
        'sedev': sedevs,
        'teacher': teachers
        })
        return HttpResponse(t.render(c))
    else:     
        sedev_id = request.POST['sedevs']
        teacher_id = request.POST['teachers']
        now = datetime.datetime.now()
        stuyear = ''
        t = 1
        if now.month>=6:
            stuyear = '%s-%s'%(now.year,now.year+1)
        else:
            stuyear = '%s-%s'%(now.year-1,now.year)
        sSedev = songoson_sedev.objects.filter(teacher_code=teacher_id, sedev_code=sedev_id)
        if not sSedev:
            songoson_sedev.objects.create(
                sedev_code = sedev_id, 
                tugsult_code = 1,
                date = datetime.date.today(),
                stu_year =  stuyear,
                teacher_code = teacher_id,
                student_code = request.user.username)
            return render_to_response('studentSedev.html',{'success':1})
        else:
            return render_to_response('studentSedev.html',{'error':1})
    return HttpResponseRedirect(reverse('sedev-student'))
 


@login_required()
def student_yzhuv(request):
    if request.method == "GET":
        yzlegs = yzleg.objects.all()
        nowyz  = yzleg.objects.filter(date__gt = datetime.date.today())
        t = loader.get_template('studentYzleg.html')
        c = Context({
        'yzlegs': yzlegs,
        'nowyz': nowyz,
        })
        return HttpResponse(t.render(c))

def contact_message(request):
    if request.method == "GET":
        return render_to_response('studentregister.html')
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
