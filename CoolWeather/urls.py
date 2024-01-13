from django.urls import path
from .views import CoolestDistricts, TravelRecommendationView

urlpatterns = [
    path('coolest-districts/', CoolestDistricts.as_view(),
         name='coolest-districts'),
    path('travel-recommendation/', TravelRecommendationView.as_view()),
]
