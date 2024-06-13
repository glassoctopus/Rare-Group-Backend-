from django.db import models
from .category import Category
from .user import User

class Post(models.Model):
  rare_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default=1) 
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=55)
  publication_date = models.DateTimeField(auto_now_add=True)
