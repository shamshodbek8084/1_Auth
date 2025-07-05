from django.urls import path
from .views import Register_View, List_Profiles

urlpatterns = [
    path('register/', Register_View.as_view(), name='register'),
    path('lists/', List_Profiles.as_view(), name='lists'),
]
