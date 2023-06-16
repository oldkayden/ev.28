from rest_framework import generics, permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from . import serializers
from .models import Category
from .serializers import CategorySerializer


class CategoryCreateListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return permissions.AllowAny(),
        return permissions.IsAdminUser(),


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny(),]
        return [permissions.IsAdminUser(),]
