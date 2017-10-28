# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField()

class Contact(models.Model):
    user = models.OneToOneField(to=User,related_name='user')
    friend = models.ManyToManyField(to=User,related_name='contacts')
