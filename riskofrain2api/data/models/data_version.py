from django.db import models


class DataVersion(models.Model):
    date = models.DateTimeField(auto_now_add=True)
