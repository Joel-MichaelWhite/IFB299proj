"""musicschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^home$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^student$', app.views.student, name='student'),
    url(r'^about', app.views.about, name='about'),
    url(r'^teacherapplication', app.views.teacherapplication, name='teacherapplication'),
    url(r'^booklesson', app.views.bookingform.as_view(), name='booklesson'),
    url(r'^updatestudent', app.views.updatestudentform.as_view(), name='updatestudent'),
    url(r'^bookingconfirmation', app.views.bookingconfirmation, name='bookingconfirmation'),
    url(r'^instrumentconfirmation', app.views.instrumentconfirmation, name='instrumentconfirmation'),
    url(r'^hireinstrument', app.views.instrumentform.as_view(), name='hireinstrument'),
    url(r'^studentshome', app.views.studentshome, name='studentshome'),
    url(r'^teachershome', app.views.teachershome, name='teachershome'),
    url(r'^teacheravailability', app.views.teacheravailability, name='teacheravailability'),
    url(r'^teacher', app.views.teacher, name='teacher'),
    url(r'^teacherbookings', app.views.teacherbookings, name='teacherbookings'),
    url(r'^updateteacher', app.views.updateteacherform.as_view(), name='updateteacher'),
    url(r'^signup', app.views.RegisterView.as_view(), name='signup'),
    url(r'^login', app.views.login_view.as_view(), name='login'),

    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    path('admin/', admin.site.urls),
]
