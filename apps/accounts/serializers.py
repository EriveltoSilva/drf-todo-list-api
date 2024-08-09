""" serializer file for user data"""
# from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# rest_framework imports
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from . import emails, utils
from .models import Lawyer, Customer, Profile

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
        fields = ('first_name', 'last_name', 'type', 'email', 'username', 'password', 'confirmation_password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True

    def validate(self, data):
        if not utils.is_email_valid(data.get('email').strip()):
            raise serializers.ValidationError("Este email tem um formato inválido", code='invalid')

        if data['password'] != data['confirmation_password']:
            raise serializers.ValidationError({"password": "As senhas são diferentes"})
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
                    project_name='Cicero PCA Advogados', company_address='',
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
        fields = ('uid', 'bi', 'bio', 'birthday', 'gender', 'phone',
                  'address', 'image', 'user')
        read_only_fields = ('id', 'uid', 'created_by', 'updated_by',)

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['user'] = UserSerializer(instance.user).data
    #     return response


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    profile = ProfileSerializer(read_only=True)

    class Meta:
        """Meta properties for user serialization"""
        model = User
        fields = ('uid', 'first_name', 'last_name', 'type', 'email', 'username', 'password', 'profile', )
        read_only_fields = ('uid',)
        extra_kwargs = {'password': {'write_only': True}}

    def __init__(self, *args, **kwargs) -> None:
        super(UserSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3


class CustomerSerializer(serializers.ModelSerializer):
    """Customer serializer"""
    class Meta:
        """Meta properties for customer serialization"""
        model = Customer
        fields = ('user',)
        read_only_fields = ('id', 'uid', 'created_by', 'updated_by',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response


class LawyerSerializer(serializers.ModelSerializer):
    """Lawyer serializer"""
    class Meta:
        """Meta properties for lawyer serialization"""
        model = Lawyer
        fields = ('order_number',
                  'hiring_date', 'area', 'user',)
        read_only_fields = ('id', 'uid', 'created_by', 'updated_by',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response
