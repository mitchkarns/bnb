from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class UserProfile(AbstractBaseUser):
    email = models.EmailField('email address', unique=True, db_index=True)
    #first_name = models.CharField(max_length=35)
    #last_name = models.CharField(max_length=35)
    is_active = models.BooleanField(default=True)
    is_org = models.BooleanField(default=False)
    region = models.CharField(max_length=100)
    num_posts = models.IntegerField(default=0)
    contact_requests = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    picture = models.ImageField(blank=True)
    #date_created = models.DateField('date created')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

