from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin URL
    path('admin/', admin.site.urls),

    # Authentication Routes
    path('auth/google', include('social_django.urls')),  # Handles social auth routes like login and callback
    path('api/auth/', include('djoser.urls')),  # Handle user authentication via djoser
    path('api/', include('djoser.urls.jwt')),  # Handle JWT authentication for APIs

    # API Routes for your apps
    path('api/', include('masters.apis.urls')),  # Include API URLs from 'masters' app
    path('api/', include('product_management.apis.urls')),  # Include API URLs from 'product_management' app
    path('api/', include('cart.apis.urls')),  # Include API URLs from 'cart' app
]

# Serve media files during development (if DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
