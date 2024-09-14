from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer
# from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse

from .models import Item


# Django generic views are just view functions (regular old python functions) that do things that are very common in web applications.
# Depending on the type of app you are building, they can save you from writing a lot of very simple views.

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


def item_list(request, *args, **kwargs):
    query_set = Item.objects.all()
    items_list = [{"title" : x.title, "price" : x.price } for x in query_set]
    data = {
        "quantity": len(items_list),
        "response": items_list,
    }
    status = 200
    return JsonResponse(data, status= status)


