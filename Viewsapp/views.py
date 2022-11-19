from django.shortcuts import render
from Modelapp.models import *
from rest_framework import viewsets

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsCategoryAdminOrReadOnly]

class SubCategoryViewSet(viewsets.ModelViewSet):

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsSubCategoryAdminOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsProductAdminOrReadOnly]

class UploadFilesViewSet(viewsets.ModelViewSet):

    queryset = UploadFiles.objects.all()
    serializer_class = UploadFilesSerializer
    permission_classes = [IsUploadFilesAdminOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserAdminOrReadOnly]