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
from rest_framework.generics import CreateAPIView

from .models import User, Comment
from .serializers import RegisterAuthorSerializer
from .serializers import CommentSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterAuthorSerializer
    # Что такое QuerySet? QuerySet, по сути, — список объектов
    # заданной модели. QuerySet позволяет читать данные из
    # базы данных, фильтровать и изменять их порядок.


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response = {
                'message': 'Комментарий успешно создан',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED, headers=headers)
        else:
            response = {
                'message': 'Комментарий не создан',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            comment = Comment.objects.get()
            comment.delete()
            response_200 = {
                "message": "Комментарий успешно удален",
            }
            return Response(response_200, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            response_404 = {
                "message": "Комментарий не найден",
            }
        return Response(response_404, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            comment = Comment.objects.get(pk=kwargs['pk'])
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_200 = {
                    "message": "Комментарий успешно обновлен",
                }
                return Response(response_200, status=status.HTTP_200_OK)
            response_400 = {
                "message": "Комментарий не обновлен",
                "errors": serializer.errors
            }
            return Response(response_400, status=status.HTTP_400_BAD_REQUEST)
        except Comment.DoesNotExist:
            response_404 = {
                "message": "Комментарий не найден",
            }
            return Response(response_404, status=status.HTTP_404_NOT_FOUND)