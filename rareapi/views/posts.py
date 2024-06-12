from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from rareapi.models.category import Category
from rareapi.models.post import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'rare_user', 'category', 'title', 'publication_date', )
        depth = 2 

class PostView(ViewSet):
    def retrieve(self, request, pk):
      try:
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data)
      except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
      posts = Post.objects.all()
      serializer = PostSerializer(posts, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

    # def create(self, request):
    #   category = Category.objects.get(pk=request.data['category'])
    #   rare_user = User.objects.get(uid=request.data['rare_user'])
      
    #   post = Post.objects.create(rare_user=rare_user, category=category, title=request.data['title'], publication_date=request.data['publication_date'])
    #   serializer = PostSerializer(post)
    #   return Response(serializer.data)

    # def update(self, request, pk):
    #   post = Post.objects.get(pk=pk)
    #   post.title = request.data['title'] 
    #   post.publication_date = request.data['date']
      
    #   category = Category.objects.get(pk=request.data['category'])
    #   post.category = category
    #   rare_user = User.objects.get(pk=request.data['rare_user'])
    #   post.rare_user = rare_user
    #   post.save()
      
    def destroy(self, request, pk):
      post = Post.objects.get(pk=pk)
      post.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
