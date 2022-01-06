from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class AuthSub(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING, related_name="supervisor")
    subordinate = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING, related_name="subordinates")

class AuthToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING)
    token = models.CharField(max_length=200, unique=True)
    expires = models.DateTimeField(default=datetime.now)

