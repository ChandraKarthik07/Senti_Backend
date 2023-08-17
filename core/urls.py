from django.urls import path, include, re_path
from .views import *

urlpatterns = [

]

urlpatterns += [
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
]