from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UrlTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    long_url = models.TextField(max_length=400)
    key_url = models.CharField(primary_key=True, max_length=100)
    data_filed =models.DateField(auto_now_add=True)
    click = models.IntegerField(default=0)

