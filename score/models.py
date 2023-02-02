from django.contrib.auth.models import User
from django.db import models


class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0)
    score_multiple = models.IntegerField(default=0)
    score_divided = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    last_check = models.DateTimeField()
    additional_column = models.CharField(null=True, blank=True, max_length=10)
