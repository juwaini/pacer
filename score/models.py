from django.contrib.auth.models import User
from django.db import models


class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0)
    score_multiple = models.IntegerField(default=0)
    last_check = models.DateTimeField()
    additional_column = models.CharField(null=True, blank=True, max_length=10)
