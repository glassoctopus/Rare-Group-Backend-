from django.db import models

class Reaction(models.Model):
    label = models.CharField(max_length=50)
    image = models.URLField(max_length=200)