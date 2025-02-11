from django.db import models
from django.contrib.auth.models import User

class CityVote(models.Model):
    city_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.city_name

class UserVote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city_vote = models.ForeignKey(CityVote, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.city_vote.city_name if self.city_vote else 'No vote'}"
