from rest_framework import serializers

from users.models import User, Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'image')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
