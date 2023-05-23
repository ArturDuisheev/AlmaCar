from django.db.migrations import serializer
from django.http import HttpResponse
from rest_framework import viewsets, status, permissions
from rest_framework import viewsets, status, permissions, mixins, serializers
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ItemAddition
from .serializers import ItemAdditionSerializer


class ItemAdditionViewSet(viewsets.ModelViewSet):
    queryset = ItemAddition.objects.all()
    serializer_class = ItemAdditionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'PUT':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'DELETE':
            self.permission_classes = [permissions.IsAdminUser]
        elif self.request.method == 'LIST':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            responce = {
                "message": "Услуга успешно создана",
                "data": serializer.data
            }
            return Response(responce, status=status.HTTP_201_CREATED, headers=headers)
        responce = {
            "message": "Ошибка при создании услуги",
            "data": serializer.errors
        }
        return Response(responce, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            headers = self.get_success_headers(serializer.data)
            responce = {
                "message": "Услуга успешно обновлена",
                "data": serializer.data
            }
            return Response(responce, status=status.HTTP_200_OK, headers=headers)
        responce = {
            "message": "Ошибка при обновлении услуги",
            "data": serializer.errors
        }
        return Response(responce, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_serializer(data=request.data).instance
        instance.delete()

