from django.db import models
import datetime

class Book(models.Model):
    title = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, blank=True)
    publish_date = models.DateField(default=datetime.date.today)  # Allow users to set the date
    

    def __str__(self):
        return self.title
