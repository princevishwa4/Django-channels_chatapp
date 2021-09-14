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
    messages = Message.objects.filter(room=room_name)
    return render(request, "chat/room.html", {'room_name': room_name, 'username': request.user.username, 'messages': messages})