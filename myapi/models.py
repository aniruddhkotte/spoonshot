from django.db import models

# Create your models here.

class Book(models.Model):
    bookId = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __self__(self):
        return self.name