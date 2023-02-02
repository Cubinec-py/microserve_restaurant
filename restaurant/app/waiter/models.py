import uuid

from django.db import models


class Waiter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
