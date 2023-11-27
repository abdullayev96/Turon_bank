from django.urls import path
from .views import *


from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('', FileAPI, basename='file'),


urlpatterns = router.urls

