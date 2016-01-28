from django.db import models


class Disp(models.Model):
    test = models.CharField(max_length=200, default="disp")
