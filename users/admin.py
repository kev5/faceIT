# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from users.models import User, Image
from django.shortcuts import get_object_or_404
from django.contrib import admin



class TagInline(admin.TabularInline):
    model = Image

class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    fields = ('username', 'first_name', 'last_name')
    inlines = (TagInline,)




admin.site.register(Image)
admin.site.register(User,UserAdmin)
