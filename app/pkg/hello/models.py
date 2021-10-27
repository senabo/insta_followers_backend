from django.db import models


class HelloMessage(models.Model):
    message = models.CharField(max_length=50)
