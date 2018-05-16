"""
Definition of forms.
"""
from django.contrib.auth.models import User
from .models import Students, Instruments
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
import datetime
from django.forms import ModelForm, Form


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class studentsbookings (forms.ModelForm):

    class Meta:
        model = Students
        fields = (
        'TeacherInstruments',
        'LessonDays',
        'LessonTime',
        'TeacherLanguageSkills',
        'TeacherGender',
        )

#For the drop down calendar
class DateInput(forms.DateInput):
    input_type = 'date'

class instrumentsform (forms.ModelForm):

    class Meta:
        model = Instruments
        fields = (
        'InstrumentType',
        'InstrumentCondition',
        'StartDate',
        'HireLength',
        )
        widgets = {
            'StartDate': DateInput(),
        }

class updateStudentForm (forms.ModelForm):

    class Meta:
        model = Students
        fields = (
        'FirstName',
        'LastName',
        'Email',
        'Address',
        'PhoneNumber',
        )