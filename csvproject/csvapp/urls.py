from django.urls import  path
from .views import *


urlpatterns = [
    path('',FileUploadView.as_view(),name='home'),
    path('parse/',parse,name='parse'),
    path('data/',DataView.as_view(),name='data'),
]