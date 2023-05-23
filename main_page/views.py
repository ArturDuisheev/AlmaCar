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

from .serializers import OurCarSerializer, DetailCarSerializer, AwardSerializer
from .models import OurCar, DetailCar, Award


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class OurCarViewSet(viewsets.ModelViewSet):
    queryset = OurCar.objects.all()
    serializer_class = OurCarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSuperuser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_201 = {
            'message': 'Машина успешно создана',
        }
        return Response(response_201, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, pk=None):
        try:
            car = OurCar.objects.get(pk=pk)
            serializer = OurCarSerializer(car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_200 = {
                    "message": "Машина успешно обновлена",
                }
                return Response(response_200, status=status.HTTP_200_OK)
            response_400 = {
                "message": "Машина не обновлена",
                "errors": serializer.errors
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
        except OurCar.DoesNotExist:
            response_404 = {
                "message": "Машина не найдена",
            }
        return Response(response_404, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            car = OurCar.objects.get(pk=pk)
            car.delete()
            response_200 = {
                "message": "Машина успешно удалена",
            }
            return Response(response_200, status=status.HTTP_200_OK)
        except OurCar.DoesNotExist:
            response_404 = {
                "message": "Машина не найдена",
            }
        return Response(response_404, status=status.HTTP_404_NOT_FOUND)


class DetailCarViewSet(viewsets.ModelViewSet):
    queryset = DetailCar.objects.all()
    serializer_class = DetailCarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSuperuser)
    parser_classes = (MultiPartParser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response = {
                'message': 'Детальная информация о машине успешно создана',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED, headers=headers)
        else:
            response = {
                'message': 'Детальная информация о машине не создана',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            car = DetailCar.objects.get(pk=pk)
            serializer = DetailCarSerializer(car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_200 = {
                    "message": "Детальная информация о машине успешно обновлена",
                }
                return Response(response_200, status=status.HTTP_200_OK)
            response_400 = {
                "message": "Детальная информация о машине не обновлена",
                "errors": serializer.errors
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
        except DetailCar.DoesNotExist:
            response_404 = {
                "message": "Машина не найдена",
            }
        return Response(response_404, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            car = DetailCar.objects.get(pk=pk)
            car.delete()
            response_200 = {
                "message": "Детальная информация о машине успешно удалена",
            }
            return Response(response_200, status=status.HTTP_200_OK)
        except DetailCar.DoesNotExist:
            response_404 = {
                "message": "Детальная информация о машине не найдена",
            }
        return Response(response_404, status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        photos = self.request.FILES.getlist('photos')[:7]  # Получаем список фотографий, ограниченный до 7
        serializer.save(photos=photos)


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    allowed_actions_for_admin = ['retrieve', 'update', 'destroy']
    allowed_actions_for_user = ['list']

    def get_permissions(self):
        if self.action in self.allowed_actions_for_admin:
            permission_classes = [permissions.IsAdminUser]
        elif self.action in self.allowed_actions_for_user:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                'message': 'Достижение успешно создано',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                'message': 'Достижение не создано',
                'errors': serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            response_data = {
                'message': 'Достижение успешно обновлено',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                'message': 'Достижение не обновлено',
                'errors': serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        response_data = {
            'message': 'Достижение успешно удалено'
        }
        return Response(response_data, status=status.HTTP_200_OK)
