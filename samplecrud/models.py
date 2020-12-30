from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(max_length=255)

    def __str__(self):
            return self.title