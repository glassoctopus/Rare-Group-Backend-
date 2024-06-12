from django.db import models
from rareapi.models.category import Category

class Post(models.Model):
  # rare_user = models.ForeignKey('rare_user', on_delete=models.CASCADE) 
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=55)
  publication_date = models.DateTimeField(auto_now_add=True)
