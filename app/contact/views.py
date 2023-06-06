from django.db.migrations import serializer
from django.http import HttpResponse
from rest_framework import viewsets, status, permissions
from rest_framework import viewsets, status, permissions, mixins, serializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        elif self.request.method == 'LIST':
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            responce = {
                "message": "Контакты успешно создан",
                "data": serializer.data
            }
            return Response(responce, status=status.HTTP_201_CREATED, headers=headers)
        responce = {
            "message": "Ошибка создания контактов",
            "data": serializer.errors
        }
        return Response(responce, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            headers = self.get_success_headers(serializer.data)
            responce = {
                "message": "Контакты успешно обновлен",
                "data": serializer.data
            }
            return Response(responce, status=status.HTTP_200_OK, headers=headers)
        responce = {
            "message": "Ошибка обновления контактов",
            "data": serializer.errors
        }
        return Response(responce, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        responce = {
            "message": "Контакты успешно удален"
        }
        return Response(responce, status=status.HTTP_200_OK)
