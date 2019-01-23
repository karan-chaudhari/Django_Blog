from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    msg = models.TextField(max_length=500)

    def __str__(self):
        return str(self.id) + " . " + self.name
