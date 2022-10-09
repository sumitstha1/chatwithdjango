from rest_framework import serializers
from .models import Room, Message

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('room', 'user', 'content', 'date_added')
        model = Message