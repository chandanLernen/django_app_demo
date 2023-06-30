from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about_index, name='about-index'),
    path('soy/', views.soy, name='soy'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
