from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrainCardViewSet

router = DefaultRouter()
router.register(r'braincards', BrainCardViewSet)

urlpatterns= [
    path('', include(router.urls))
]
