from django.urls import path
from . import views
from .views import (
    UserPostListView
    
)


app_name = 'users'

urlpatterns = [
 
    
     path('register/', views.register, name='register'),
     path('profile/', views.profile, name='profile'),
     path('<str:username>/', UserPostListView.as_view(), name='user-posts'),


]