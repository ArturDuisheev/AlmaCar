from rest_framework import viewsets, status, permissions, generics, mixins
from datetime import date, timedelta

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from draw.models import Game, OpenedBox, Winner, Prize
from draw.serializers import GameSerializer, OpenedBoxCreateSerializer
from draw.permissions import HaveTryPermission


class GameViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | permissions.IsAdminUser]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in self.permission_classes]


class OpenBoxAPIView(generics.CreateAPIView):
    queryset = OpenedBox.objects.all()
    serializer_class = OpenedBoxCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        game = Game.objects.get(pk=self.kwargs['pk'])
        if not game.is_active:
            return Response({"message": "Game is not active"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        if Prize.objects.filter(index=serializer.validated_data.get('index')).exists():
            return Response({
                "message": "You won a prize!",
                "prize": Prize.objects.get(index=serializer.validated_data.get('index'))
            }, headers=headers, status=status.HTTP_200_OK)
        else:
            return Response({
                "messgae": "You opened empty box!",
            }, headers=headers, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()
        if serializer.validated_data.get('index'):
            if Prize.objects.filter(index=serializer.validated_data.get('index')).exists():
                Winner.objects.create(user=self.request.user,
                                      prize=Prize.objects.get(index=serializer.validated_data.get('index')))
