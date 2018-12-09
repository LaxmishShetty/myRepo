# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User)


    #additional info if required apart from User fields
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(blank=True,upload_to='profile_pics')

    def __str__(self):
        return self.user.username
