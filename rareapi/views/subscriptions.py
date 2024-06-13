"""View module for handling requests about subscriptions"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Subscription, User

class SubscriptionView(ViewSet):
  """Subscription view"""
  
  def retrieve(self, request, pk):
    """Handle GET requests to get a single subscription"""
    try:
      subscription = Subscription.objects.get(pk=pk)
      serializer = SubscriptionSerializer(subscription)
      return Response(serializer.data)
    except Subscription.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests to get a list of all subscriptions"""
    subscriptions = Subscription.objects.all()
    serializer = SubscriptionSerializer(subscriptions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def create(self, request):
    """Handle POST requests to create a subscription"""
    follower_id = User.objects.get(pk=request.data['followerId'])
    author_id = User.objects.get(uid=request.data['authorId'])
    
    subscription = Subscription.objects.create(
      follower_id = follower_id,
      author_id = author_id,
      created_on = request.data['created_on'],
      ended_on = request.data['ended_on'],
    )
    serializer = SubscriptionSerializer(subscription)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def destroy(self, request, pk):
    """Handle DELETE request for a subscription"""
    subscription = Subscription.objects.get(pk=pk)
    subscription.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

class SubscriptionSerializer(serializers.ModelSerializer):
  """JSON serializer for subscriptions"""
  class Meta:
    model = Subscription
    fields = ('id', 'follower_id', 'author_id', 'created_on', 'ended_on')
    depth = 1
    