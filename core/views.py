
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Prefetch
from rest_framework import status
from .models import Channels, Videos
from .serializers import  VideoSerializer,ChannelSerializer

def home(request):
    return HttpResponse("Hello, karthik")

class ChannelInfoAPIView(APIView):
    def get(self, request, channel_id, format=None):
        try:
            channel = Channels.objects.get(channel_id=channel_id)
            channel_serializer = ChannelSerializer(channel)
            videos = channel.videos_set.all()
            videos_serializer = VideoSerializer(videos, many=True)
            
            response_data = {
                'channel': channel_serializer.data,
                'videos': videos_serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Channels.DoesNotExist:
            return Response({"error": "Channel not found"}, status=status.HTTP_404_NOT_FOUND)








# class ChannelInfoAPIView(generics.RetrieveAPIView):
#     queryset = Channels.objects.select_related('videos').prefetch_related(
#         Prefetch('videos', queryset=Videos.objects.only('vid_id', 'vid_title'))
#     )
#     serializer_class = ChannelInfoSerializer
#     lookup_field = 'channel_id'