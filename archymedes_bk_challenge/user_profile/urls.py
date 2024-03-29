from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('users/', ProfileView.as_view(), name="get_post_users"),
    path('users/<int:user_id>', ProfileView.as_view(), name="update_delete_user")
]