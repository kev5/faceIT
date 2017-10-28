# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from users.models import User, Contact
from users.serializers import UserSerializer, ContactSerializer


class CreateUser(CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateContact(CreateAPIView):
    queryset = Contact.objects.filter()
    serializer_class = ContactSerializer
    # permission_classes = ('IsAuthenticated',)