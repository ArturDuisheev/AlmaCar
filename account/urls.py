from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="Register"),
    path('comments/', views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name="Comments"),
    path('comments/<int:pk>/', views.CommentViewSet.as_view({'get':'retrieve', 'put': 'update', 'delete': 'destroy`'})),
    path('', include('rest_framework.urls')),
    path('obtain_token/', obtain_auth_token, name='token'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh')

]

