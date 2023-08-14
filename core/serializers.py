from rest_framework import serializers
from .models import Channels, Videos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class ChannelSerializer(serializers.ModelSerializer):
    # videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Channels
        fields = '__all__'

class ChannelInfoSerializer(serializers.Serializer):
    channel = ChannelSerializer()
    videos = VideoSerializer(many=True)
