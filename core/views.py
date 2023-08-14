
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status
from .models import Channels, Videos
from .serializers import ChannelInfoSerializer, VideoSerializer,ChannelSerializer

def home(request):
    return HttpResponse("Hello, karthik")

class ChannelVideosListView(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        channel_id = self.kwargs['channel_id']
        return Videos.objects.filter(channel=channel_id)

class ChannelInfoAPIView(APIView):
    def get(self, request, channel_id, format=None):
        try:
            channel = Channels.objects.get(channel_id=channel_id)
            videos = Videos.objects.filter(channel=channel.channel_id)
            serializer = ChannelInfoSerializer({
                'channel': channel,
                'videos': videos
            })

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Channels.DoesNotExist:
            return Response({"error": "Channel not found"}, status=status.HTTP_404_NOT_FOUND)

