from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
import datetime


# class UserProfileManager(BaseUserManager):
#     def create_user(self, email, first_name=None, last_name=None, region=None, password=None, date_created=None):
#         user = self.model(email=email, first_name=first_name, last_name=last_name,
#                           region=region, password=password, date_created=date_created)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password, first_name, last_name, date_created, region):
#         user = self.create_user(email=email, first_name=first_name, last_name=last_name,
#                           region=region, password=password, date_created=date_created)
#         user.save()
#         return user
#
# class UserProfile(AbstractBaseUser):
#     email = models.EmailField('email address', unique=True, db_index=True)
#     first_name = models.CharField(max_length=35)
#     last_name = models.CharField(max_length=35)
#     is_active = models.BooleanField(default=True)
#     is_org = models.BooleanField(default=False)
#     region = models.CharField(max_length=100)
#     num_posts = models.IntegerField(default=0)
#     contact_requests = models.IntegerField(default=0)
#     rating = models.IntegerField(default=0)
#     picture = models.ImageField(blank=True)
#     date_created = models.DateField('date created')
# #     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = UserProfileManager()
#
#     def __unicode__(self):
#         return self.email

class MyUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, region, date_created,
                    is_org, num_posts, contact_requests, rating, picture):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), password=password, first_name=first_name,
                          last_name=last_name, region=region, date_created=date_created, is_org=is_org,
                          num_posts=num_posts, contact_requests=contact_requests, rating=rating, picture=picture)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name, region, date_created,
                         is_org=False, num_posts=0, contact_requests=0, rating=0, picture=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password, first_name, last_name, region, date_created,
                                is_org, num_posts, contact_requests, rating, picture)
        user.is_admin = True
        user.save(using=self._db)
        return user


class TestProfile(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    is_org = models.BooleanField(default=False)
    region = models.CharField(max_length=100)
    num_posts = models.IntegerField(default=0)
    contact_requests = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    picture = models.ImageField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
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


class Post(models.Model):
    # user is UserProfile class that created this
    # status is Boolean where true is active
    # region is String region house is in
    # sub_region is String sub_region house is in
    # distance is String distance to dxe community space (empty if no community space)
    # house_type is List of String [floor, couch, spare bed] converted by json
    # provided is List of String [pillows, towels, shower, blankets, wifi, laundry] converted by json
    # proximity is String distance to public transportation
    # num_people is Integer number of people house can host
    # date_created is datetime date created
    user = models.OneToOneField(TestProfile)
    status = models.BooleanField(default=True)
    region = models.CharField(max_length=100)
    sub_region = models.CharField(max_length=100)
    title = models.TextField()
    distance = models.TextField()
    house_type = models.TextField()
    provided = models.TextField()
    proximity = models.TextField()
    num_people = models.IntegerField()
    notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
