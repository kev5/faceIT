# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.views import APIView

from users.models import User, Contact
from users.serializers import UserSerializer, ContactSerializer
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.response import Response
from .face_detection import face_detection
from .face_recognizer import image_recognition
from django.core.files.storage import default_storage
import os
import tempfile


class CheckImage(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self,request):
        return Response(template_name='takeImage.html')

    def post(self,request):
#        do some processing
        image = request.FILES['image']
        path = 'tmp.jpg'
        f = open(path, 'w') # open the tmp file for writing
        f.write(image.read()) # write the tmp file
        f.close()
        face_detection(path)
        id= image_recognition(path)
        if id == -1:
            mesg= "Not found"
        else:
            mesg = UserSerializer(User.objects.get(pk=id)).data
        print mesg
        return HttpResponse(mesg,content_type='application/json')


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
