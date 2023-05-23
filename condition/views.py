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

from .models import CardInCondition
from .serializers import CardInConditionSerializer


class CardInConditionViewSet(ModelViewSet):
    queryset = CardInCondition.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CardInConditionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

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
            response = {
                "message": "Карточка с условием успешно создана",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED, headers=headers)
        response = {
            "message": "Ошибка создания карточки с условием",
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            if 'image' in request.data and request.data['image'] is None:
                instance.image_field_name.delete(save=False)
                del request.data['image']
            self.perform_update(serializer)
            headers = self.get_success_headers(serializer.data)
            response = {
                "message": "Карточка с условием успешно обновлена",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK, headers=headers)
        response = {
            "message": "Ошибка обновления карточки с условием",
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        responce = {
            "message": "Карточка с условием успешно удалена"
        }
        return Response(responce, status=status.HTTP_200_OK)
