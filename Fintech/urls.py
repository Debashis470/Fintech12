from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Swagger imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version='v1',
        description="Simple JWT Auth API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Root welcome message
def root_message(request):
    return JsonResponse({'message': 'Welcome to the Django API backend'})

urlpatterns = [
    path('', root_message),
    path('admin/', admin.site.urls),

    # ✅ Direct API endpoints without /api/ prefix
    path('', include('accounts.urls')),  

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
