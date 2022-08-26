from django.shortcuts import render
from rest_framework import generics
from .models import Book, Cart, Product, category
from .serializer import BookSerializer, CartSerializer, CategorySerializer,ProductSerializer,UserSerializer,RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from EcommerceApp.permissions import Is_owner
from rest_framework.response import Response
import uuid
from rest_framework import status
from rest_framework import serializers

# Create your views here.

class RegistrationApi(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self,request):
        serializer =self.get_serializer(data=request.data)
        #serializer.is_valid(raise_exception = True)
        #serializer.save() 
        if serializer.is_valid():
            serializer.save()
            return Response({
                'Requestid':str(uuid.uuid()),
                'message':'user created succesfully',
                'user':serializer.data},
                status= status.HTTP_201_CREATED
                )
        return Response({'errors':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

class ListCategory(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Is_owner]
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Is_owner]
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class ListBooks(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Is_owner]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Is_owner]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListProduct(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Is_owner]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Is_owner]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListUser(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Is_owner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Is_owner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListCart(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Is_owner]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,Is_owner]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    
