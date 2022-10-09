from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import RoomSerializer

# API View
class RoomApiView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        context = {
            "status_code": 200,
            "message": "Kathmandu",
            "Data": serializer.data,
            "error": []
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

@login_required
def rooms(request):
    template = 'room/rooms.html'
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }

    return render(request, template, context)

@login_required
def room(request, slug):
    template = 'room/room.html'
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    context = {
        'room': room,
        'messages': messages
    }

    return render(request, template, context)