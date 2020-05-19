from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Chat, Contact
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
import json

User = get_user_model()


@login_required
def room(request, room_name):
    create_or_not_contact(request.user.email)
    return render(request, 'messenger/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.first_name)),
        'email': mark_safe(json.dumps(request.user.email))
    })

def add_all_users():
    user=User.objects.all()
    return user
def create_or_not_contact(email):
    user = User.objects.get(email=email)
    try:
        contact = Contact.objects.get(user=user)
    except Contact.DoesNotExist:
        contact = Contact.objects.create(user=user)
        contact.save()


def get_last_10_messages(chatID):
    chat = get_object_or_404(Chat, id=chatID)
    return chat.messages.order_by('-timestamp').all()[:10]


def get_user_contact(email):
    user = get_object_or_404(User, email=email)
    return get_object_or_404(Contact, user=user)


def verify_participants(participants):
    for email in participants:
        user = User.objects.get(email=email)


def get_current_chat(chatID):
    return get_object_or_404(Chat, id=chatID)
