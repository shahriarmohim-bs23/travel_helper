from django.urls import path
from .views import CoolestDistricts
urlpatterns = [
    path('coolest-districts/', CoolestDistricts.as_view(),
         name='coolest-districts'),
]
