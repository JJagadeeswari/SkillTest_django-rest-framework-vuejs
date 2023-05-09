from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.core.validators import RegexValidator

from .utils import user_profile_pic_path

from django.contrib.postgres.fields import ArrayField, JSONField


# Create your models here
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=254, null=True)
    last_name = models.CharField(max_length=254, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}, {self.role}'

    class Meta:
        db_table = 'Role'


class UserProfile(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    id = models.AutoField(primary_key=True)
    profile_pic = models.ImageField(upload_to=user_profile_pic_path, blank=True)
    user_id = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, default=2)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, default=+000000000)
    designation = models.CharField(max_length=50, default="None")
    experiance = models.IntegerField(default=0)
    interest = models.CharField(max_length=200, default="None")
    #preferred_tech = models.CharField(max_length=200, default="General")
    technology_name = models.CharField(max_length=200, default="General")
    #technology_name = ArrayField(models.CharField(max_length=200))
    #technology_name = ArrayField(models.CharField(max_length=200, default=["General"]))
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}, {self.user_id}, {self.role_id}'
    
    class Meta:
        db_table = 'UserProfile'


class Logs(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    error_info = models.TextField()
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}, {self.user_id}'
    
    class Meta:
        db_table = 'Logs'

