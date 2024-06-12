from django.db import models
from .user import User
import datetime

class Subscription(models.Model):
  follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
  author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
  created_on = models.DateField(default=datetime.date(2024, 6, 11))
  ended_on = models.DateField(default=datetime.date(2024, 6, 11))
