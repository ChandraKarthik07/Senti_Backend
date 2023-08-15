
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Prefetch
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import uuid,hashlib
from .tests import scrape_channel
from .serializers import  *

from rest_framework_simplejwt.views import TokenObtainPairView
def home(request):
    return HttpResponse("Hello, karthik")


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        self.serializer_class.request = request
        return super().post(request, *args, **kwargs)


class UserSignupView(APIView):
    permission_classes = (AllowAny,)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class GenerateScanView(APIView):
    def get(self, request):
        # Get user_uuid and channel_name from query parameters
        user_uuid = request.GET.get("user_uuid")
        channel_name = request.GET.get("channel_name")

        # Check if user_uuid and channel_name are provided
        if not user_uuid or not channel_name:
            return Response({"error": "user_uuid and channel_name are required."}, status=400)

        try:
            # Get the User instance using the provided user_uuid
            user = User.objects.get(uuid=user_uuid)
        except User.DoesNotExist:
            return Response({"error": "User not found with the provided user_uuid."}, status=404)

        # Generate a scan_id UUID
        text_to_hash = channel_name+str(timezone.now())
        hashed_value = hashlib.sha256(text_to_hash.encode()).hexdigest()

        # Create a new ScanTable entry
        scan_entry = ScanTable.objects.create(
            scan_id=hashed_value,
            user=user,  # Assign the User instance
            scan_channel=channel_name,
            scan_date_time=timezone.now()
        )

        response_data = {
            "scan_id": hashed_value
        }
        scrape_channel(channel_name, hashed_value)
        return Response(response_data)   


class ChannelInfoAPIView(APIView):
    def get(self, request, channel_id, format=None):
        try:
            channel = Channels.objects.get(scan_id=channel_id)
            print(channel)
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