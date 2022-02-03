from django.urls import path
from .views import ProfileView

app_name = 'user_profile'

urlpatterns = [
    path('users/', ProfileView.as_view())
]