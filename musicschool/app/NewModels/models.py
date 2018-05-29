from django.db import models

# creating some variables that will be used
UserType = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('admin','Admin'),
)

SEX = (
    ('male', 'Male'),
    ('female', 'Female'),
)
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
Instrumentcond = (
    ('new', 'New'),
    ('excellent', 'Excellent'),
    ('good', 'Good'),
    ('repair', 'Repair'),
    ('discard', 'Discard'),
)
SkillLevel=(
    ('expert','Expert'),
    ('high','High'),
    ('medicore','Medicore'),
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
HIREDURATION = (
    ('1', '1 week'),
    ('2', '2 weeks'),
    ('3', '3 weeks'),
    ('4', '4 weeks'),
    ('5', '5 weeks'),
    ('6', '6 weeks'),
    ('7', '7 weeks'),
    ('8', '8 weeks'),
)

TIMES = (('7','7am'),
         ('8','8am'),
         ('9','9am'),
         ('10','10am'),
         ('11','11am'),
         ('12','12pm'),
         ('13','1pm'),
         ('14','2pm'),
         ('15','3pm'),
         ('16','4pm'),
         ('17','5pm'),
         ('18','6pm'),
         ('19','7pm'))


LESSONDAYS = (
        ('mon', 'Mon'),
        ('tues', 'Tues'),
        ('wed', 'Wed'),
        ('thurs', 'Thurs'),
        ('fri', 'Fri'),
        ('sat', 'Sat'),
        ('sun', 'Sun'),
    )
Booleanchoice = (
    ('full', 'Full'),
    ('empty', 'Empty'),
)

#Creating models

class Users (models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    Email = models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    UserType=models.CharField(max_length=10 , choices=UserType)
    DOB = models.DateField(),
    Address = models.CharField(max_length=100)
    sex = models.CharField(max_length=7, choices=SEX)
    FacebookID = models.IntegerField(null=True, blank=True)

class PhoneNumbers(models.Model):
    PhoneNumber = models.CharField(primary_key=True, max_length=15)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)

class Instruments(models.Model):
    InstrumentType = models.CharField("Instrument", choices=INSTRUMENT, max_length=20)
    InstrumentCondition = models.CharField("Condition", max_length=9, choices=Instrumentcond)
    HireCost = models.IntegerField()
    Hiredby = models.ForeignKey(Users, on_delete=models.CASCADE,null=True, blank=True)

class TeacherInstruments(models.Model):
        InstrumentType=models.CharField("InstrumentSkillLevel",choices=INSTRUMENT,max_length=20)
        InstrumentSkillLevel=models.CharField("InstrumentSkillLevel",choices=SkillLevel,max_length=20)
        TeacherID=models.ForeignKey(Users, on_delete=models.CASCADE)

class TeacherLanguage(models.Model):
        LanguageSkillLevel=models.CharField("LanguageSkillLevel",choices=SkillLevel,max_length=20)
        Languages=models.CharField("Languages",choices=Languages,max_length=20)
        TeacherID=models.ForeignKey(Users, on_delete=models.CASCADE)

class Contract(models.Model):
    StudentID=models.ForeignKey(Users,on_delete=models.CASCADE,related_name="Users_Student_Contract")
    TeacherID = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="Users_Teacher_Contract")
    StartDate=models.DateField()
    EndDate=models.DateField()




class TeacherAvailability(models.Model):
    TeacherID=models.ForeignKey(Users,on_delete=models.CASCADE, related_name="Users_Teacher_Availibility")
    Days=models.CharField("Days",choices=LESSONDAYS, max_length=20)
    Times=models.CharField("Times", choices=TIMES, max_length=15)
    StudentID = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name="Users_Student_Availibility")




