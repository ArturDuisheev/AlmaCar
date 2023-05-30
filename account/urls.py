from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="Register"),
    path('comments/', views.CommentViewSet.as_view({'post': 'list', 'get': 'destroy'}), name="Comments"),
    path('', include('rest_framework.urls')),
    path('token/', obtain_auth_token),
]