"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import UserForm, studentsbookings


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def teacherapplication(request):
    """Renders the teacher application page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/teacherapplication.html',
        {
            'title':'Teacher Application',
            'message':'The page for potential teachers to apply.',
            'year':datetime.now().year,
        }
    )
def signup(request):
    """Renders the sign up page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/signup.html',
        {
            'title':'Student Sign up',
            'message':'The page for students to sign up.',
            'year':datetime.now().year,
        }
    )

def student(request):
    """Renders the sign up page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/student.html',
        {
            'title':'Student Profile Page',
            'message':'This is the student profile page.',
            'year':datetime.now().year,
        }
    )

def studentshome(request):
    """Renders the sign up page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/studentshome.html',
        {
            'title':'Student Home Page',
            'message':'This is the student home page.',
            'year':datetime.now().year,
        }
    )
def booklesson(request):
    """Renders the sign up page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/booklesson.html',
        {
            'title':'Book Lesson Page',
            'message':'This is the lesson booking page page.',
            'year':datetime.now().year,
        }
    )

def bookingconfirmation(request):
    """Renders the booking confirmation page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/bookingconfirmation.html',
        {
            'title':'Booking Confirmation',
            'message':'Here is the booking you just made.',
            'year':datetime.now().year,
        }
    )

def hireinstrument(request):
    """Renders the sign up page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/hireinstrument.html',
        {
            'title':'Instrument Hire Page',
            'message':'This is the instrument hire page.',
            'year':datetime.now().year,
        }
    )

class UserFormView(View):
    form_class = UserForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'app/signup.html', {'form' : form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('studentshome')

        return render(request, 'app/signup.html', {'form': form})

class bookingform(View):
    form_class = studentsbookings

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'app/booklesson.html', {'form' : form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('studentshome')

        return render(request, 'app/booklesson.html', {'form': form})

# def signupform(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('app/index.html')
#     else:
#         form = SignupForm
#         args = {'form' : form}
#         return (request, 'app/signup.html', args)