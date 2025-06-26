from django.urls import path, include

urlpatterns = [
    path("v1/", include('braincards.urls')),
    path("v1/", include('brainspaces.urls')),
    path("v1/", include('tags.urls'))
]