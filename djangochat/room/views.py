from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

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