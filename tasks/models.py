from django.db import models
from mongoengine import Document, StringField, BooleanField, DateTimeField
import datetime


# Create your models here.
class Task(models.Model): 
    title = models.CharField(max_length=80)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MongoTask(Document):
    title = StringField(max_length=80, required=True)
    description = StringField()
    is_completed = BooleanField(default=False)
    date = DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.title
