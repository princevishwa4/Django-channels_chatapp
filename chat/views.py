import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from chat.forms import RoomForm
from chat.models import Room, Message


@login_required(login_url='/auth/login/')
def home(request):
    context = {}
    room_names = RoomForm()

    context['user'] = request.user
    context['room_names'] = room_names
    return render(request, "chat/home.html", context)


def room(request, room_name, *args, **kwargs):
    roomname = ""
    room_names = Room.objects.all()
    if room_name.isdigit():
        for name in room_names:
            if name.id == int(room_name):
                roomname = name.name

    else:
        roomname = room_name
        if not Room.objects.filter(name=roomname).exists():
            room = Room(name=roomname)
            room.save()
    messages = Message.objects.filter(room=roomname)
    return render(request, "chat/room.html", {'room_name': roomname, 'username': request.user.username, 'messages': messages})