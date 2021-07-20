# parsed_data/models.py
from django.db import models


class LostarkData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
