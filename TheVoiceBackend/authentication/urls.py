from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),    

    path('user/', views.UserListView.as_view(), name='user'),
    path('dashboard/', views.MentorCandiatesListView.as_view(), name='dashboard'),
]
