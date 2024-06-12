import datetime
from django.db import models

class User(models.Model):
    
    first_name = models.CharField(max_length=69)
    last_name = models.CharField(max_length=69)
    bio = models.CharField(max_length=666)
    profile_image_url = models.CharField(max_length=666)
    email = models.CharField(max_length=100)
    created_on = models.DateField(default=datetime.date(2024, 6, 11))
    active = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    uid = models.CharField(max_length=69)
