# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Image(models.Model):
    name = models.ImageField()
    user = models.ForeignKey(User)





class Contact(models.Model):
    user = models.OneToOneField(to=User, related_name='user')
    friend = models.ManyToManyField(to=User, related_name='contacts')
