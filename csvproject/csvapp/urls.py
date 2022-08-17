from django.urls import  path
from .views import *


urlpatterns = [
    path('',index,name='home'),
    path('parse/',parse,name='parse'),
    path('data/',DataView.as_view(),name='data'),
]