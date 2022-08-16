from django.urls import  path
from .views import *


urlpatterns = [
    path('',CsvToModel.as_view(),name='home'),
]