from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

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
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = UserProfileManager()
#
#     def __unicode__(self):
#         return self.email
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyU(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
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

    def __str__(self):              # __unicode__ on Python 2
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
