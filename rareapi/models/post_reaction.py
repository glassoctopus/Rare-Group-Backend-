from django.db import models
from .user import User
from .post import Post
from .reaction import Reaction

class PostReaction(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)