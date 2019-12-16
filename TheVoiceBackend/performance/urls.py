from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('candidate/<int:pk>/', views.CandiateMentorScoreListView.as_view(), name='candidate'),
]
