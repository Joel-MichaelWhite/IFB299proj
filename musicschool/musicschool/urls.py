"""musicschool URL Configuration. The URLS are configured
so that a certain URL returns a certain view.


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
