"""View module for handling requests about subscriptions"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Subscription

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
    """Hand GET requests to get a list of all subscriptions"""
    subscriptions = Subscription.objects.all()
    serializer = SubscriptionSerializer(subscriptions, many=True)
    return Response(serializer.data)
  
class SubscriptionSerializer(serializers.ModelSerializer):
  """JSON serializer for subscriptions"""
  class Meta:
    model = Subscription
    fields = ('id', 'follower_id', 'author_id', 'created_on', 'ended_on')
    depth = 1
    