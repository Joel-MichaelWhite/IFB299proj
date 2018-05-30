"""
Definition of forms.
"""
# from django.contrib.auth.models import User
from .models import Students
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
import datetime
from django.forms import ModelForm, Form
# from django.views.generic import CreateView, FormView
from django.contrib.auth import get_user_model
from .user_accounts.models import *
from app.user_accounts.models import Instruments
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User = get_user_model()

class loginform(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)


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

class DateInput(forms.DateInput):
    input_type = 'date'

class instrumentsform (forms.ModelForm):

    class Meta:
        model = Instruments
        fields = (
        'InstrumentType',
        'InstrumentCondition',
        'HireCost',
        'Hiredby',
        )

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UpdateStudentForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','DOB','Address','sex')
        widgets = {
            'DOB': DateInput(),
        }

class UpdateTeacherForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','DOB','Address','sex')
        widgets = {
            'DOB': DateInput(),
        }


class Registerform(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    Address = forms.CharField(max_length=100)
    sex = forms.ChoiceField(choices=SEX)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',
                  'first_name',
                  'last_name',
                  'DOB',
                  'Address',
                  'sex',
                  'password1',
                  'password2')
        widgets = {
            'DOB': DateInput(),
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(Registerform, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
