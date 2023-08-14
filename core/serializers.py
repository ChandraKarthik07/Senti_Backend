from rest_framework import serializers
from .models import Channels, Videos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channels
        fields = '__all__'


