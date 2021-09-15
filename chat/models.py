from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)        