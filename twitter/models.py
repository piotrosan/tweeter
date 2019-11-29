from django.db import models


class LastSync(models.Model):
    tweet_id = models.IntegerField()
    date = models.DateTimeField()
