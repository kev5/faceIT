from rest_framework import serializers

from users.models import User, Contact, Image


class ImageSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')

    class Meta:
        model = Image
        fields = ('name', 'user_id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',)
        depth = 1


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
