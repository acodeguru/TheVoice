from django.db import models 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils import timezone
import uuid

# Create your models here.
class Performance (models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    candidate=models.ForeignKey(User, on_delete=models.CASCADE)
    song_name=models.CharField(max_length=100,blank=True)
    event_date=models.DateField(editable=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=(('candidate','event_date'),)

class PerformanceScore (models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    performance=models.ForeignKey(Performance,on_delete=models.CASCADE)
    mentor=models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.IntegerField(blank=False, default=0)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=(('performance','mentor'),)
