from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class one_x_one(models.Model):
    qs   = models.CharField(max_length=250)
    ans  = models.IntegerField()
    user = models.ForeignKey(User)
