""" api module form Users views endpoints """

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated

from . import utils, emails
from .permissions import IsOwnerOrAdmin
from .models import Profile
from .serializers import ProfileSerializer
from .serializers import UserSerializer, UserRegisterSerializer, MyTokenObtainPairSerializer

User = get_user_model()


# * -------------------- Authentication --------------------------------
class MyTokenObtainPairView(TokenObtainPairView):
    """my customized obtain token class with some user data in token generated"""
    serializer_class = MyTokenObtainPairSerializer


class PasswordResetEmailVerifyView(generics.RetrieveAPIView):
    """user view to generate a password reset email"""
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer

    def get_object(self):
        email = self.kwargs['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None  # Handling User not found case

        user.otp = utils.generate_otp()
        user.save()
        return user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        if user is None:
            return Response(
                {"status": "error", "message": "Não existe um usuário com este e-mail"},
                status=status.HTTP_404_NOT_FOUND
            )

        uidb64 = user.uid
        otp = user.otp
        link = f'http://localhost:5173/create-new-password?otp={otp}&uidb64={uidb64}'
        if not settings.DEBUG:
            try:
                emails.send_password_reset(user, user.email, settings.SYSTEM_NAME, '', link)
            except Exception as e:
                # Show email do user with link in terminal
                print("Error sending email for reset password\n-->", e)
                print("#"*100, 'Clique aqui:', link, "#"*100, sep='\n')
        else:
            print("#"*100, 'Clique aqui:', link, "#"*100, sep='\n')

        serializer = self.get_serializer(user)
        return Response(serializer.data)


class PasswordChangeView(generics.CreateAPIView):
    """ a password view to change the user password"""
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        otp = request.data['otp']
        uidb64 = request.data['uidb64']
        password = request.data['password']
        confirmation_password = request.data['confirmation_password']

        if password != confirmation_password:
            return Response(
                {"status": "error", "message": "As senhas são diferentes"},
                status=status.HTTP_304_NOT_MODIFIED
            )
        elif len('password') < 8:
            return Response(
                {"status": "error", "message": "As senhas devem ter no mínimo 8 caracteres"},
                status=status.HTTP_304_NOT_MODIFIED
            )

        user = User.objects.filter(id=uidb64, otp=otp)
        if user:
            user = user.first()
            user.set_password(password)
            user.otp = ""
            user.save()
            return Response(
                {"status": "success", "message": "Palavra-Passe alterada com Sucesso"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"status": "error", "message": "Ocorreu um erro ao alterar a palavra-passe"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# * -------------------- Users --------------------------------
class UserListView(generics.ListAPIView):
    """User list endpoint."""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class UserCreateView(generics.CreateAPIView):
    """User view form for creating a new user endpoint."""
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrAdmin, )
    lookup_field = "id"


# * -------------------- Profiles --------------------------------
class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)


class ProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """profile user detail view to retrieve profile information"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    # def get_object(self, *args, **kwargs):
    #     user_id = self.kwargs.get('user_id')
    #     try:
    #         user = User.objects.get(uid=user_id)
    #         profile = Profile.objects.get(user=user)
    #     except Profile.DoesNotExist:
    #         profile = None
    #     return profile

    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile is None:
            return Response({"status": "error", "message": "Perfil não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        profile = self.get_object()
        if profile is None:
            return Response({"status": "error", "message": "ID do perfil inválido!"}, status=status.HTTP_404_NOT_FOUND)

        # Include the user in the request data before serializing
        request.data['user'] = profile.user.id
        serializer = self.get_serializer(profile, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
