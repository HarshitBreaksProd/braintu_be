from django.urls import include, path
from rest_framework.routers import DefaultRouter

from braintu_be.brainspaces.views import BrainSpaceViewset

router = DefaultRouter()
router.register(r'brainspaces', BrainSpaceViewset)

urlpatterns = [
    path('', include(router.urls))
]
