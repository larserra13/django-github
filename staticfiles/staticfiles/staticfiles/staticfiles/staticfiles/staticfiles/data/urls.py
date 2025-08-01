from django.urls import path
from data import views

#app_name = "data"

urlpatterns = [
    path('', views.indexViews, name='index_url'),
    path('about', views.aboutViews, name='about_url'),
    path('contact', views.contactViews, name='contact_url'),
]
