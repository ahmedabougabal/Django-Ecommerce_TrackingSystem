# ecommerce/urls.py
from django.contrib import admin
from django.urls import path, include
from tracking_system.views import home, track_orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ts/', home),
    path('ts/track_orders', track_orders, name='track_orders'),
    path('', include('mart.urls', namespace='mart')),
    path('Products/', include('Products.urls')),
    path('mart/', include('mart.urls', namespace='mart')),
    path('authentication/', include('authentication.urls')),
]