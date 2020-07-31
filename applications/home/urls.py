from django.contrib import admin
from django.urls import path
from .views import HomeView, HomeListView

urlpatterns = [
    path('list/', HomeListView.as_view()),
]