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
        fields = ('first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid', 'id')

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
        """Get all Users"""
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
            email=request.data["email"],
            is_staff=False,
            uid=request.data["uid"],
        )
        
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        """PUT / Update a User"""
        try:
            user = User.objects.get(pk=pk)
            data = request.data

            # Debug: print request data
            print("Request data:", data)

            # Update fields if present in request data
            user.first_name = data.get("first_name", user.first_name)
            user.last_name = data.get("last_name", user.last_name)
            user.bio = data.get("bio", user.bio)
            user.profile_image_url = data.get("profile_image_url", user.profile_image_url)
            user.email = data.get("email", user.email)
            user.active = data.get("active", user.active)
            user.is_staff = data.get("is_staff", user.is_staff)

            user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        """DELETE / Delete a User"""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
