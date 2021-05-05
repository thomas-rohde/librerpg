from django.shortcuts import render
from rest_framework import generics
from .serializer import RoomSerializer
from .models import Room

# Create your views here.

class RoomView(generics.ListAPIView): #return all the room objects to a way to view
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
