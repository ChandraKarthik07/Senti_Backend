from django.urls import path,include
from .views import ChannelInfoAPIView,home
urlpatterns=[
    path("home/",home,name="test"),
    path("channel/<str:channel_id>/",ChannelInfoAPIView.as_view(),name="channel-info"),
    # path('videos-by-channel/<str:channel_id>/', VideosByChannelAPIView.as_view(), name='videos-by-channel'),

]