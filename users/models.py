from django.db import models
from django.contrib.auth.models import User

class AuthSub(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING, related_name="supervisor")
    subordinate = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING, related_name="subordinates")
