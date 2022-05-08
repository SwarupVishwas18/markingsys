from unicodedata import name
from django.urls import path
from . import views
import django.contrib.auth.views as views_aut

app_name = 'marks'

urlpatterns = [
    path('', views.index, name='index'),
    path('addData', views.addData, name='addData')
]
