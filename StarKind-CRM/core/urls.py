from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (token_refresh, token_obtain_pair)

schema_view = get_schema_view(
   openapi.Info(
      title="StarKind CRM",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('token/', token_obtain_pair, name='token'),
    path('token/refresh/', token_refresh, name='token-refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
