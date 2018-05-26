from django.db import models
# from NewModels.models import Users, PhoneNumbers, Instruments, TeacherInstruments, TeacherLanguage, Contract, TeacherAvailability
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

SEX = (
    ('male', 'Male'),
    ('female', 'Female'),
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

    DOB = models.DateField()
    Address = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=7, choices=SEX, blank=True, null=True)
    FacebookID = models.IntegerField(null=True, blank=True)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS= []

    objects = UserManager()

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

