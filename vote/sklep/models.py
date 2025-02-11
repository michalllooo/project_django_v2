from django.db import models

class CityVote(models.Model):
    city_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.city_name
