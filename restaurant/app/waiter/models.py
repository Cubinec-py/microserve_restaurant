import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Waiter(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']
