from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListView
router = DefaultRouter()
router.register('students', ListView, basename='student')
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
