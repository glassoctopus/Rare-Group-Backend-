from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from rareapi.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'label', ]

class CategoryView(ViewSet):
    def retrieve(self, request, pk):
      category = Category.objects.get(pk=pk)
      serializer = CategorySerializer(category, context={'request': request})
      return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
      categories = Category.objects.all()
      category = request.query_params.get('category', None)
      if category is not None:
            categories = categories.filter(category_id=category)
      serializer = CategorySerializer(categories, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
