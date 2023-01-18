from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from app.authenticate.models import User

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
class UserCreationSerializers(DynamicFieldsModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=100)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']





    def validate(self, attrs):
        super().validate(attrs)
        username_exists = User.objects.filter(username=attrs['username']).exists()
        email_exists = User.objects.filter(email=attrs['email']).exists()
        phone_number_exists = User.objects.filter(phone_number=attrs['phone_number']).exists()

        if username_exists:
            raise serializers.ValidationError(detail='User with username exists')

        if email_exists:
            raise serializers.ValidationError(detail='User with email exists')

        if phone_number_exists:
            raise serializers.ValidationError(detail='User with number exists')

        return attrs
