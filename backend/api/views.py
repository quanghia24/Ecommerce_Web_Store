from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


# Django generic views are just view functions (regular old python functions) that do things that are very common in web applications.
# Depending on the type of app you are building, they can save you from writing a lot of very simple views.

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]




