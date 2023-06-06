from django.db.migrations import serializer
from django.http import HttpResponse
from rest_framework import viewsets, status, permissions
from rest_framework import viewsets, status, permissions, mixins, serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenViewBase
from django.contrib.auth import authenticate
from .models import User, Comment, MyProfile, Bonus
from .serializers import RegisterUserSerializer, ContactSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CommentSerializer, MyTokenObtainPairSerializer, \
    ProfileSerializer, BonusUserSerializer


class MyTokenObtainPairView(TokenViewBase):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        user = authenticate(phone_number=phone_number)

        if user is not None:
            token = RefreshToken.for_user(user)
            token['phone_number'] = user.phone_number
            return Response({'token': str(token.access_token)})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)


class MyTokenRefreshView(TokenRefreshView):
    pass


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = RegisterUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response = {
                    "message": "Регистрация прошла успешно!",
                    "data": serializer.data
                }
                # PromoCode.objects.create(code=promo_code, user=serializer.data['id'])
                return Response(data=response)
            else:
                data = serializer.errors
                return Response({"message": "Что-то пошло не так!",
                                 "data": data})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


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
        instance = self.get_object()
        instance.delete()
        responce = {
            "message": "Комментарий успешно удален"
        }
        return Response(responce, status=status.HTTP_204_NO_CONTENT)

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


class ContactView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ContactSerializer


class MyProfileView(viewsets.ModelViewSet):
    queryset = MyProfile.objects.all()
    serializer_class = ProfileSerializer


class BonusUserView(viewsets.ModelViewSet):
    queryset = Bonus.objects.all()
    serializer_class = BonusUserSerializer


