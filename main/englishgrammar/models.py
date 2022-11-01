from django.db import models


class getGram1(models.Model):
    PoS = models.CharField(max_length=100)
    count = models.PositiveIntegerField()

# grammar_app_post
