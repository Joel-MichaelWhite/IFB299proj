#
#
from django.db import models
#
# Creating some public variables to use within different model classes
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

Languages = (
        ('english', 'English'),
        ('chinese', 'Chinese'),
        ('spanish', 'Spanish'),
        ('hindi', 'Hindi'),
        ('arabic', 'Arabic'),
        ('portuguese', 'Portuguese'),
        ('bengali', 'Bengali'),
        ('russian', 'Russian'),
        ('japanese', 'Japanese'),
        ('punjabi', 'Punjabi'),

    )

SEX = (
    ('male', 'Male'),
    ('female', 'Female'),
)

LESSONDAYS = (
        ('mon', 'Mon'),
        ('tues', 'Tues'),
        ('wed', 'Wed'),
        ('thurs', 'Thurs'),
        ('fri', 'Fri'),
        ('sat', 'Sat'),
        ('sun', 'Sun'),
    )


class Students (models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    DOB = models.DateField()
    Address = models.CharField(max_length=100)
    sex = models.CharField(max_length=7, choices=SEX)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    FacebookID = models.IntegerField()

    TeacherInstruments = models.CharField(max_length=20, choices=INSTRUMENT)
    LessonDays = models.CharField(max_length=5, choices=LESSONDAYS)
    LessonTime = models.DateTimeField()

    TeacherLanguageSkills = models.CharField(max_length=10, choices=Languages)

    TeacherGender = models.CharField(max_length=7, choices=SEX)


class Admins (models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    DOB = models.DateField()
    sex = models.CharField(max_length=7, choices=SEX)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    FacebookID = models.IntegerField()


class Teachers (models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    DOB = models.DateField()
    Qualifications = models.CharField(max_length=100)
    sex = models.CharField(max_length=7, choices=SEX)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    FacebookID = models.IntegerField()
    Instruments = models.CharField(max_length=20, choices=INSTRUMENT)


class Instruments (models.Model):
    InstrumentType = models.CharField(choices=INSTRUMENT, max_length=20)
    HireCost = models.IntegerField
    Instrumentcond = (
        ('new', 'New'),
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('repair', 'Repair'),
        ('discard', 'Discard'),
    )
    InstrumentCondition=models.CharField(max_length=9, choices=Instrumentcond)


class InstrumentHire (models.Model):
    Student = models.ForeignKey(Students, on_delete=models.CASCADE)
    Instrument = models.ForeignKey(Instruments, on_delete=models.CASCADE)
    StartDate = models.DateField()
    EndDate = models.DateField()


class TeachingSchedule (models.Model) :
    Teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    TeachingDays = models.CharField(choices=LESSONDAYS, max_length=5)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Booleanchoice= (
        ('full', 'Full'),
        ('empty', 'Empty'),
    )
    ScheduleStatus = models.CharField(choices=Booleanchoice, max_length=4)


class Contract (models.Model) :
    StartDate = models.DateField()
    EndDate = models.DateField()
    LessonDays = models.CharField(choices=LESSONDAYS, max_length=5)
    LessonTimes = models.TimeField()
    LessonType = models.CharField(choices=INSTRUMENT, max_length=20)
    Cost = models.IntegerField()
    Student = models.ForeignKey(Students, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)


class TeacherFeedback (models.Model) :
    Teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    SKILLRATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    InstrumentSkill = models.CharField(choices=SKILLRATING, max_length=1)
    LanguageSkill = models.CharField(choices=SKILLRATING,max_length=1)
    TeachingSkill = models.CharField(choices=SKILLRATING, max_length=1)
    FeedbackComment = models.CharField(max_length=100)
