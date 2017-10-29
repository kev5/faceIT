# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.views import APIView

from users.models import User, Contact
from users.serializers import UserSerializer, ContactSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


class CheckImage(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self,request):
        return Response(template_name='takeImage.html')

    def post(self,request):
#        do some processing
        print request.data
        return Response(dict(mesg=''),template_name='takeImage.html')


class CreateUser(CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListeUser(ListAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateContact(CreateAPIView):
    queryset = Contact.objects.filter()
    serializer_class = ContactSerializer
