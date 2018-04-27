"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

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
