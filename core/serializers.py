from rest_framework import serializers
from .models import Channels, Videos
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channels
        fields = '__all__'


class MonthlyStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monthlystats
        fields = '__all__'

class VideoStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videostats
        fields = '__all__'
