from django.db import models

# Create your models here.
class Event(models.Model):
    name=models.TextField(max_length=50)
    info=models.TextField(max_length=500)
    text=models.TextField(max_length=500)

    def __str__(self):
        return self.text