from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title=f"{settings.SYSTEM_NAME} Backend API",
        default_version='v1',
        description=F"{settings.SYSTEM_NAME} is a WEB API for accessing ToDo list App",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=settings.EMAIL_HOST_USER),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('apps.accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
