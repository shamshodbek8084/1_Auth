from django.urls import path
from .views import Register_View, List_Profiles, Login_View

urlpatterns = [
    path('register/', Register_View.as_view(), name='register'),
    path('lists/', List_Profiles.as_view(), name='lists'),
    path('login/', Login_View.as_view(), name='login'),
]
