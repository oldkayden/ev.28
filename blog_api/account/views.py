from dj_rest_auth.views import LogoutView
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from like.serializers import FavoriteSerializer
from . import serializers


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserListSerializer
        return serializers.UserDetailSerializer

    @action(['get'], detail=True)
    def favorites(self, request, pk):
        user = self.get_object()
        fav_posts = user.favorutes.all()
        serializers = FavoriteSerializer(fav_posts, many=True)
        return Response(serializers.data, status=200)


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserListSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserDetailSerializer
#     permission_classes = (permissions.IsAuthenticated,)
