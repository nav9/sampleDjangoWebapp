from django.urls import path

from . import views

app_name = 'landingPage' #namespace

urlpatterns = [
    path('', views.index, name='index'),
]
