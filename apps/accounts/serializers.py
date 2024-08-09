""" serializer file for user data"""
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from . import emails
from . import validators
from .models import Profile

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['username'] = user.username
        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmation_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'confirmation_password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True

    def validate(self, data):
        errors_messages = {}

        if not validators.is_email_valid(data.get('email').strip()):
            errors_messages["email"] = "Este e-mail tem um formato inválido"

        if not validators.is_password_equal(data['password'], data['confirmation_password']):
            errors_messages["password"] = errors_messages["confirmation_password"] = "As senhas são diferentes"

        if errors_messages:
            raise serializers.ValidationError(errors_messages)
        return data

    def create(self, validated_data):
        validated_data.pop('confirmation_password')
        user = User.objects.create_user(**validated_data)

        email_user, _ = user.email.split("@")
        user.username = validated_data['username'] if validated_data['username'] else email_user
        user.set_password(validated_data['password'])
        user.save()
        link = "http://127.0.0.1:5171/accounts/login/"
        try:
            if not settings.DEBUG:
                emails.send_register_welcome(
                    user, user.email,
                    project_name=settings.SYSTEM_NAME, company_address='',
                    action_url='http://127.0.0.1:8000/accounts/login/', support_email='',
                    login_url=link, project_website=''
                )
            else:
                print("#"*100, link, "#"*100, sep="\n")
        except Exception as e:
            print("Error sending email", e)
            print("#"*100, link, "#"*100, sep="\n")
        return user


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer"""
    class Meta:
        """Meta properties for profile serialization"""
        model = Profile
        fields = ('id', 'bio', 'birthday',
                  'gender', 'phone', 'address',
                  'image', 'user', )
        read_only_fields = ('id', 'user')


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    # profile = ProfileSerializer(read_only=True)

    class Meta:
        """Meta properties for user serialization"""
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'profile', )
        read_only_fields = ('id', 'profile',)
        extra_kwargs = {'password': {'write_only': True}, }
