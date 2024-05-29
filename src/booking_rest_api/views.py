from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
# from booking_app.models import User
from booking_app.models import Hotel_owner
from booking_app.models import Hobby
from rest_framework import status


from .serializers import UserSerializer
from .serializers import OwnerSerializer
from .serializers import HobbySerializer

class SomeDataView(APIView):
    def get(self, request, format=None):
        data = {"message": "Hello, wold!"}
        return Response(data)


class UserApiView(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        users = User.objects.get(pk=pk)
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        user = UserSerializer(data=request.data)

        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OwnerApiView(APIView):

    def get(self, request, format=None):
        owner = Hotel_owner.objects.all()
        serializer = UserSerializer(owner, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        owner = Hotel_owner.get(pk=pk)
        serializer = UserSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        owner = UserSerializer(data=request.data)

        if owner.is_valid():
            owner.save()
            return Response(owner.data, status=status.HTTP_201_CREATED)
        return Response(owner.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        owner = Hotel_owner.objects.get(pk=pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HobbyApiView(APIView):

    def get(self, request, format=None):
        hobby = Hobby.objects.all()
        serializer = HobbySerializer(hobby, many=True)
        return Response(serializer.data)