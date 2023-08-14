from django.urls import path,include
from .views import *
urlpatterns=[
    path("home/",home,name="test"),
    path("channel/<str:channel_id>/",ChannelInfoAPIView.as_view(),name="channel-info"),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

]