from django.urls import path

from . import views

app_name = 'listings'


urlpatterns = [
     path('', views.real_estate_index, name='real_estate_index'),
     path('add-listing/', views.listing_create, name='listing_create'),
     path('<pk>/', views.listing_retrieve, name='listing_retrieve'),
     path('<pk>/edit/', views.listing_update, name='listing_retrieve'),
     path('<pk>/delete/', views.listing_delete, name='listing_delete'),
    


]
