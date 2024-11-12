from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.views import APIView
from. models import MenuItems
from .serializers import MenuItemSerializer
# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer
    
    
class DestroyUpdateMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer
    

