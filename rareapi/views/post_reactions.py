from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Reaction, User, Post, PostReaction

class PostReactionView(ViewSet):

    def retrieve(self, request, pk):
        try:
            post_reaction = PostReaction.objects.get(pk=pk)
            serializer = PostReactionSerializer(post_reaction)
            return Response(serializer.data)
        except post_reaction.DoesNotExist:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) # type: ignore
        
    def list(self, request):
        post_reactions = PostReaction.objects.all()
        serializer = PostReactionSerializer(post_reactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        reaction = Reaction.objects.get(pk=request.data["reaction_id"])
        rare_user = User.objects.get(pk=request.data['rare_user_id'])
        post = Post.objects.get(pk=request.data['post_id'])

        post_reaction = PostReaction.objects.create(
            rare_user=rare_user, 
            reaction=reaction,
            post=post,
        )

        serializer = PostReactionSerializer(post_reaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        
            post_reaction = PostReaction.objects.get(pk=pk)
            post_reaction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class PostReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReaction
        fields = ('id', 'rare_user', 'reaction','post')
        depth = 1
