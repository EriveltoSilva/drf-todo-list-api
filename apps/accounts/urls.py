"""api system endpoints"""
from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Authentication
    path('token/', views.MyTokenObtainPairView.as_view(), name="token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('password/reset/<str:email>/', views.PasswordResetEmailVerifyView.as_view()),
    path('password/change/', views.PasswordChangeView.as_view(), name="api-password_change"),

    # Users endpoints
    path('users/', views.UserListView.as_view(), name="api-user-list"),
    path('users/create/', views.UserCreateView.as_view(), name="api-user-create"),
    path('users/<uuid:id>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='api-user-delete'),

    # ! Create, Read, Update, Delete
    # Profile endpoints
    path('profiles/', views.ProfileListAPIView.as_view(), name='api-profile-list'),
    path('profiles/<uuid:id>/', views.ProfileRetrieveUpdateView.as_view(), name='api-profile-retrieve-update'),
]
