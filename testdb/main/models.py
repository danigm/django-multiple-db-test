from django.db import models


class Main(models.Model):
    test = models.CharField(max_length=200, default="main test")
