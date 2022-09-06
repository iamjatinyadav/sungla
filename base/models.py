from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django_extensions.db.models import TimeStampedModel
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active= True, is_staff= False, is_admin= False):
        if not email:
            raise ValueError("user must have an email address")
        if not password:
            raise ValueError("user must have a password")
        user_obj = self.model(
            email= self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.save(using = self._db)
        return user_obj

    def create_staffuser(self, email, password = None):
        user = self.create_user(
            email,
            password=password,
            is_staff= True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin = True
        )
        return user


class User(AbstractBaseUser):
    email= models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.CharField(max_length=30, null=True, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    organisation = models.ManyToManyField('Organisation', related_name="user_orgnization", through='Userorg')


    USERNAME_FIELD = 'email'

    REQUIRED_FIELD = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True




    def get_full_name(self):
        return self.email 

    def get_short_name(self):
        return self.email 

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

class Glasses(models.Model):
    image = models.FileField(upload_to="media/")
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self) -> str:
        return 'Message from '+ self.name



class Organisation(TimeStampedModel):
    
    name = models.CharField(max_length=30, null=False, blank=False) 
    city = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        verbose_name="organisation"

    def __str__(self):
        return self.name




class Userorg(TimeStampedModel):
    ROLES = (
        ('Develpoer', 'Developer'),
        ('Tester','Tester'),
        ('QA','QA'),
        ('Manager','Manager'),
        ('Team Lead','Team Lead')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, null=True, choices=ROLES, default='Developer',unique=True)
    
    class Meta:
        verbose_name = "Userorg"

    def __str__(self):
        return self.user.first_name + ' in ' + self.organisation.name + ' as a '+ self.role

    def organisation_count(self, obj):
        return obj.organisation.count()









   






