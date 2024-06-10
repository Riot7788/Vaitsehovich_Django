from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from  rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
# from booking_app.models import User
from booking_app.models import Hotel_owner
from booking_app.models import Hobby
from rest_framework import status
from rest_framework.authentication import (
    SessionAuthentication,
    BaseAuthentication,
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated

from .paginations import CustomPagination
from .serializers import UserSerializer
from .serializers import OwnerSerializer
from .serializers import HobbySerializer

class SomeDataView(APIView):
    def get(self, request, format=None):
        data = {"message": "Hello, wold!"}
        return Response(data)


class UserApiView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # pagination_class = [CustomPagination]
    filter_fields = ['username']
    search_fields = ['first_name', 'last_name', 'username']

# class UserApiView(APIView):
#
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         users = User.objects.get(pk=pk)
#         serializer = UserSerializer(users, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def post(self, request, format=None):
#         user = UserSerializer(data=request.data)
#
#         if user.is_valid():
#             user.save()
#             return Response(user.data, status=status.HTTP_201_CREATED)
#         return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         user = User.objects.get(pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class OwnerApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Hotel_owner.objects.all()
    serializer_class = OwnerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['first_name', 'last_name']

    # def get(self, request, format=None):
    #     owner = Hotel_owner.objects.all()
    #     serializer = UserSerializer(owner, many=True)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     owner = Hotel_owner.get(pk=pk)
    #     serializer = UserSerializer(owner, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def post(self, request, format=None):
    #     owner = UserSerializer(data=request.data)
    #
    #     if owner.is_valid():
    #         owner.save()
    #         return Response(owner.data, status=status.HTTP_201_CREATED)
    #     return Response(owner.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     owner = Hotel_owner.objects.get(pk=pk)
    #     owner.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class HobbyApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']

    # def get(self, request, format=None):
    #     hobby = Hobby.objects.all()
    #     serializer = HobbySerializer(hobby, many=True)
    #     return Response(serializer.data)