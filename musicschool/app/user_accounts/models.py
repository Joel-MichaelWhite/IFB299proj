#importing django models class as well as some functionality for the users

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Creating some CHOICE variables, which function and are used in a similar manner
# to the ENUM datatype in other programming languages
#

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

SEX = (
    ('male', 'Male'),
    ('female', 'Female'),
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

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, DOB, Address, sex, FacebookID, password=None,  is_student=True, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a correct password")
        user_obj = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            DOB = DOB,
            Address = Address,
            sex = sex,
            FacebookID = FacebookID
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.student = is_student
        user_obj.save(using=self.db)
        return user_obj
    def create_staffuser(self, email,first_name, last_name, DOB, Address, sex, FacebookID, password=None):
        user = self.create_user(
            email,
            first_name,
            last_name,
            DOB,
            Address,
            sex,
            FacebookID,
            password=password,
            is_student=True,
            is_staff=True
        )
        return user

    def create_superuser(self, email,first_name, last_name, DOB, Address, sex, FacebookID, password=None):
        user = self.create_user(
            email,
            first_name,
            last_name,
            DOB,
            Address,
            sex,
            FacebookID,
            password=password,
            is_staff=True,
            is_student=True,
            is_admin=True
        )
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    student = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)

    DOB = models.DateField(null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=7, choices=SEX, blank=True, null=True)
    FacebookID = models.IntegerField(null=True, blank=True)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS= []

    objects = UserManager()

# returning email field when user object is referenced

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
#
# All the models used in various sections of the Student, Teacher and Admin
# pages, also used as tables in the AWS database, through running migrations.


class Instruments(models.Model):

    InstrumentType = models.CharField("Instrument", choices=INSTRUMENT, max_length=20)
    InstrumentCondition = models.CharField("Condition", max_length=9, choices=Instrumentcond)
    HireCost = models.IntegerField()
    Hiredby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, default=True, choices=False)

class TeacherInstruments(models.Model):
    InstrumentType = models.CharField("InstrumentSkillLevel", choices=INSTRUMENT, max_length=20)
    InstrumentSkillLevel = models.CharField("InstrumentSkillLevel", choices=SkillLevel, max_length=20)
    if User.staff is True:
        TeacherID = models.ForeignKey(User.first_name, on_delete=models.CASCADE)


class TeacherLanguage(models.Model):
    LanguageSkillLevel = models.CharField("LanguageSkillLevel", choices=SkillLevel, max_length=20)
    Languages = models.CharField("Languages", choices=Languages, max_length=20)
    if User.staff is True:
        TeacherID = models.ForeignKey(User, on_delete=models.CASCADE)


class Contract(models.Model):
    if User.student is True:
        StudentID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Users_Student_Contract")
    if User.staff is True:
        TeacherID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Users_Teacher_Contract")
    StartDate = models.DateField()
    EndDate = models.DateField()


class TeacherAvailability(models.Model):
    if User.student is True:
        TeacherID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Users_Teacher_Availibility")
    Days = models.CharField("Days", choices=LESSONDAYS, max_length=20)
    Times = models.CharField("Times", choices=TIMES, max_length=15)
    if User.staff is True:
        StudentID = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                                  related_name="Users_Student_Availibility")

class LessonBookings(models.Model):
    StudentID=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="Lesson_bookings_StudentID")
    TeacherID=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="Lesson_bookings_TeacherID")
    StudentFirstName = models.CharField(max_length=100, null=True)
    StudentLastName = models.CharField(max_length=100, null=True)
    TeacherFirstName = models.CharField(max_length=100, null=True)
    TeacherLastName = models.CharField(max_length=100, null=True)
    TeacherInstrument = models.CharField(max_length=100, null=True, choices=INSTRUMENT)
    TeacherLanguage = models.CharField(max_length=100, null=True, choices=Languages)
    LessonStartTime = models.CharField("LessonStartTime", choices=TIMES, max_length=20)
    LessonEndTime = models.CharField("LessonEndTIme", choices=TIMES, max_length=20)
    LessonDay = models.CharField("LessonDay", choices=LESSONDAYS, max_length=20)
