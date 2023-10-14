from django.db import models
from datetime import datetime

# Create your models here.

class TodoTable(models.Model):
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.text}' 