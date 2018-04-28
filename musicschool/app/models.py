#
#
from django.db import models
#
#
class Students(models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    DOB = models.DateField()
    Address = models.CharField(max_length=100)
    SEX = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    sex = models.CharField(max_length=7, choices=SEX)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    FacebookID = models.CharField(max_length=121)
    TEACHERINSTRUMENT = (
        ('acousticguitar', 'Acoustic Guitar'),
        ('electricguitar', 'Electric Guitar'),
        ('bassguitar', 'Bass Guitar'),
        ('piano', 'Piano'),
        ('cello', 'Cello'),
        ('drums', 'Drums'),
        ('violin', 'Violin'),
        ('saxophone', 'Saxophone'),
        ('harmonium', 'Harmonium'),
        ('tablas', 'Tablas'),
        ('santurs', 'Santurs'),
        ('vina', 'Vina'),
    )
    TeacherInstruments = models.CharField(max_length=20, choices=TEACHERINSTRUMENT)
    LESSONDAYS = (
        ('mon', 'Mon'),
        ('tues', 'Tues'),
        ('wed', 'Wed'),
        ('thurs', 'Thurs'),
        ('fri', 'Fri'),
        ('sat', 'Sat'),
        ('sun', 'Sun'),
    )
    LessonDays = models.CharField(max_length=5, choices=LESSONDAYS)
    LessonTime = models.DateTimeField()
    TEACHERLANGUAGESKILLS = (
        ('english', 'English'),
        ('chinese', 'Chinese'),
    )
    TeacherLanguageSkills = models.CharField(max_length=10, choices=TEACHERLANGUAGESKILLS)
    TEACHERGENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    TeacherGender = models.CharField(max_length=7, choices=TEACHERGENDER)

class Admins(models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    DOB = models.DateField()
    SEX = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    sex = models.CharField(max_length=7, choices=SEX)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    FacebookID = models.CharField(max_length=121)

class Teachers(models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    DOB = models.DateField()
    Qualifications = models.CharField(max_length=100)
    SEX = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    sex = models.CharField(max_length=7, choices=SEX)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    FacebookID = models.CharField(max_length=121)
    INSTRUMENT = (
        ('acousticguitar', 'Acoustic Guitar'),
        ('electricguitar', 'Electric Guitar'),
        ('bassguitar', 'Bass Guitar'),
        ('piano', 'Piano'),
        ('cello', 'Cello'),
        ('drums', 'Drums'),
        ('violin', 'Violin'),
        ('saxophone', 'Saxophone'),
        ('harmonium', 'Harmonium'),
        ('tablas', 'Tablas'),
        ('santurs', 'Santurs'),
        ('vina', 'Vina'),
    )
    Instruments = models.CharField(max_length=20, choices=INSTRUMENT)





