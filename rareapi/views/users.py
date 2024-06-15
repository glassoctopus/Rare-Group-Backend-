"""View module for handling requests about Users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import User
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid')

def get_current_date_formatted():
    """helper time/date stamp"""
    current_date = timezone.now().date()
    return current_date.strftime('%Y-%m-%d')
class UserView(ViewSet):
    """User View for simple social full stack app"""
    
    def retrieve(self, request, pk):
        """Get a User"""
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list(self, request):
        """Get all Artist, get all artist by genre"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        """POST / Create a User"""
        user = User.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            bio=request.data["bio"],
            profile_image_url=request.data["profile_image_url"],
            created_on=get_current_date_formatted(),
            is_staff=False,
            uid=request.data["uid"],
        )
        
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """PUT / Update a User"""
        user = User.objects.get(pk=pk)
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.bio = request.data["bio"]
        user.profile_image_url = request.data["profile_image_url"]
        user.is_staff=request.data["is_staff"]
        user.save()
        
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)