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
from .tests import *
from .serializers import  *
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
User=get_user_model()

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
        print(user_uuid,channel_name)
        # Check if user_uuid and channel_name are provided
        if not user_uuid or not channel_name:
            return Response({"error": "user_uuid and channel_name are required."}, status=400)

        try:
            # Get the User instance using the provided user_uuid
            user = User.objects.get(id=user_uuid)
            print(user)
        except User.DoesNotExist:
            return Response({"error": "User not found with the provided user_uuid."}, status=404)

        # Generate a scan_id UUID
        k=timezone.now()
        text_to_hash = channel_name+str(k)
        hashed_value = hashlib.sha256(text_to_hash.encode()).hexdigest()[:10]

        # Create a new ScanTable entry
        print(hashed_value)
        scan_entry = scanTable.objects.create(
            user=user,  # Assign the User instance
            scan_id=hashed_value,
            channel_name=channel_name,
            scan_date=k
        )
        print(scan_entry)
        response_data = {
            "scan_id": hashed_value
        }
        scrape_channel(channel_name, hashed_value)
        return Response(response_data)   


class ChannelInfoAPIView(APIView):
    def get(self, request, scan_id, format=None):
        try:
            channel = Channels.objects.get(scan_id=scan_id)
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


class MonthlyStatsAPIView(APIView):
    def get(self, request, scan_id):
        try:
            monthly_stats = Monthlystats.objects.filter(channel__scan_id=scan_id)
            serializer = MonthlystatsSerializer(monthly_stats, many=True)
            ready_to_plot = process_data(serializer.data)
            return Response(ready_to_plot)
        except Monthlystats.DoesNotExist:
            return Response({"message": "Monthly stats not found for the given scan_id."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class VideoStatsAPIView(APIView):
    def get(self, request, scan_id):
        try:
            videostats = Videostats.objects.filter(channel__scan_id=scan_id)
            serializer = VideoStatsSerializer(videostats, many=True)
            # ready_to_plot=process_videostats(serializer.data)
            return Response(serializer.data)
        except Videostats.DoesNotExist:
            return Response({"message": "Video stats not found for the given scan_id."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
##change