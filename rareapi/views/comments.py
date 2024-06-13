from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment

class CommentView(ViewSet):
    def retrieve(self, request, pk):
      comment = Comment.objects.get(pk=pk)
      serializer = CommentSerializer(comment, context={'request': request})
      return Response(serializer.data, status=status.HTTP_200_OK)
      
    def list(self, request):
      comments = Comment.objects.all()
      serializer = CommentSerializer(comments, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
          
    def create(self, request):
      serializer = CommentSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
              
    def update(self, request, pk):
      comment = Comment.objects.get(pk=pk)
      serializer = CommentSerializer(comment, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
          
    def delete(self, request, pk):
      comment = Comment.objects.get(pk=pk)
      comment.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
          
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Comment
      fields = ['id', 'author', 'post', 'content', 'created_on']
