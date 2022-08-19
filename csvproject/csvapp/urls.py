from django.urls import  include, path
from .views import *


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('',FileUploadView.as_view(),name='home'),
    path('parse/',ParseView.as_view(),name='parse'),
    path('data/',DataView.as_view(),name='data'),
]