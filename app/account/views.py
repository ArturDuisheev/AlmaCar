from rest_framework import viewsets, status, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenViewBase
from django.contrib.auth import authenticate
from .models import User, Comment
from .serializers import RegisterUserSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CommentSerializer, MyTokenObtainPairSerializer
from .permissions import IsAuthenticatedOrObjectOwner

from main_page.serializers import DetailCarSerializer, ActiveDetailCarSerializer
from main_page.models import DetailCar
from draw.models import Winner


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


class AccountListAPIView(viewsets.generics.ListAPIView):

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer

    def get_permissions(self):
            return [permissions.IsAuthenticatedOrReadOnly()]


class AccountDetailAPIView(viewsets.generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrObjectOwner]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticatedOrObjectOwner()]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]


class CarLizingHistory(viewsets.generics.ListAPIView):
    def get_queryset(self):
        return DetailCar.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        return DetailCarSerializer

    def get_permissions(self):
        return [permissions.IsAuthenticatedOrReadOnly()]


class DrowListAPIView(viewsets.generics.ListAPIView):
    def get_queryset(self):
        return Winner.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        return DetailCarSerializer

    def get_permissions(self):
        return [permissions.IsAuthenticatedOrReadOnly()]


