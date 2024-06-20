from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment
from .users import UserSerializer, User
from .posts import Post

class CommentView(ViewSet):
    def retrieve(self, request, pk):
      comment = Comment.objects.get(pk=pk)
      serializer = CommentSerializer(comment, context={'request': request})
      return Response(serializer.data, status=status.HTTP_200_OK)
      
    def list(self, request):
        post_id = request.query_params.get('post_id', None)
        if post_id is not None:
            comments = Comment.objects.filter(post_id=post_id)
        else:
            comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


          
    def create(self, request):
        author_id = request.data.get('author', None)
        post_id = request.data.get('post', None)
        content = request.data.get('content', None)

        if author_id and post_id and content:
            author = User.objects.filter(pk=author_id).first()
            post = Post.objects.filter(pk=post_id).first()

            if author and post:
                comment = Comment.objects.create(author=author, post=post, content=content)
                serializer = CommentSerializer(comment, context={'request': request})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid author or post'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

              
    def update(self, request, pk):
      comment = Comment.objects.get(pk=pk)
      serializer = CommentSerializer(comment, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
          
    def destroy(self, request, pk):
        comment = Comment.objects.filter(pk=pk).first()
        if comment:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


          
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_on']
