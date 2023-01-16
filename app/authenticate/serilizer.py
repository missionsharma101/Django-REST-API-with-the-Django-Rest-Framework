from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from app.authenticate.models import User


class UserCreationSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=100)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        email_exists = User.objects.filter(username=attrs['email']).exists()

        if username_exists:
            raise serializers.ValidationError(detail='User with username exists')

        if email_exists:
            raise serializers.ValidationError(detail='User with username exists')
