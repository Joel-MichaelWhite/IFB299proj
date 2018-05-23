"""
Definition of forms.
"""
# from django.contrib.auth.models import User
from .models import Students, Instruments
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
import datetime
from django.forms import ModelForm, Form
# from django.views.generic import CreateView, FormView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User = get_user_model()



# class BootstrapAuthenticationForm(AuthenticationForm):
#     """Authentication form which uses boostrap CSS."""
#     username = forms.CharField(max_length=254,
#                                widget=forms.TextInput({
#                                    'class': 'form-control',
#                                    'placeholder': 'User name'}))
#     password = forms.CharField(label=_("Password"),
#                                widget=forms.PasswordInput({
#                                    'class': 'form-control',
#                                    'placeholder':'Password'}))
# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password']

# class RegisterForm(forms.ModelForm):
#     FirstName = forms.CharField(max_length=60, unique=True)
#     LastName = forms.CharField(max_length=60, unique=True)
#     DOB = forms.DateField()
#     Address = forms.CharField(max_length=100, unique=True)
#     sex = forms.CharField(max_length=7, choices=SEX)
#     PhoneNumber = forms.CharField(max_length=15, unique=True)
#     Email = forms.EmailField(max_length=100, unique=True)
#     FacebookID = .IntegerField()
#
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('')

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
        'HireCost',
        'InstrumentCondition',
        'StartDate',
        'HireLength',
        )
        widgets = {
            'StartDate': DateInput(),
        }

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

class Registerform(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','first_name', 'last_name',)

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