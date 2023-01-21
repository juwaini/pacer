from django.contrib.auth.models import User
from django.db import models


class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0)
    last_check = models.DateTimeField()