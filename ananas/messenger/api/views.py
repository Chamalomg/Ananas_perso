from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
import json
from messenger.models import Chat
from .serializers import ChatSerializer, UserSerializer

User = get_user_model()


def get_user_contact(email):
    user = get_object_or_404(User, email=email)
    return user


class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Chat.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            contact = get_user_contact(email)
            queryset = contact.chats.all()
        return queryset


class AllUser(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class ChatPublic(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Chat.objects.filter(status='Public')
        return queryset


class ChatDetailView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny,)


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def partial_update(self, request, *args, **kwargs):
        """update le model mais partiellement PATCH"""
        instance = self.get_object()
        update_fields = []

        for user in request.data['participants']:
            u = User.objects.get(email=user)
            instance.participants.add(u)
        for user in request.data['admin']:
            u = User.objects.get(email=user)
            instance.admin.add(u)
        if request.data['name'] != '':
            instance.name = request.data['name']
            update_fields.append('name')

        instance.save(update_fields=update_fields)

        return Response()


class AdminPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_object_permission(self, request, view, *args, **kwargs):
        chat = args[0]
        if request.user in chat.admin.all():
            return True
        else:
            return False


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (AdminPermission,)
