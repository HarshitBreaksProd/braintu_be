from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagViewset

router = DefaultRouter()
router.register(r'tags', TagViewset)

urlpatterns = [
    path('', include(router.urls))
]
