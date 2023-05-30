from rest_framework import viewsets, status, permissions
from datetime import date, timedelta

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Box, Prize, MoreInfo
from .serializers import BoxSerializer, PrizeSerializer,MoreInfoSerializer


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
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


class PrizeViewSet(viewsets.ModelViewSet):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
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


# class RentalViewSet(viewsets.ModelViewSet):
#     queryset = Rental.objects.all()
#     serializer_class = RentalSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly | IsAdminUser]
#
#     def get_permissions(self):
#         if self.request.method == 'POST':
#             self.permission_classes = [permissions.IsAdminUser]
#         elif self.request.method == 'PUT':
#             self.permission_classes = [permissions.IsAdminUser]
#         elif self.request.method == 'DELETE':
#             self.permission_classes = [permissions.IsAdminUser]
#         elif self.request.method == 'LIST':
#             self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#         return [permission() for permission in self.permission_classes]
#
#     def list(self, request, *args, **kwargs):
#         thirty_days_ago = date.today() - timedelta(days=30)
#         rentals = Rental.objects.filter(start_date__gte=thirty_days_ago, user__profile__isnull=False)
#         serializer = self.get_serializer(rentals, many=True)
#         return Response(serializer.data)


class MoreInfoViewSet(viewsets.ModelViewSet):
    queryset = MoreInfo.objects.all()
    serializer_class = MoreInfoSerializer
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
        if serializer.is_valid():
            serializer.save()
            responce = {
                'status': 'success',
                'message': 'More info added successfully',
                'data': serializer.data
            }
            return Response(responce, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            responce = {
                'status': 'success',
                'message': 'More info updated successfully',
                'data': serializer.data,
            }
            return Response(responce, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        responce = {
            'status': 'success',
            'message': 'More info deleted successfully',
        }
        return Response(responce, status=status.HTTP_200_OK)
