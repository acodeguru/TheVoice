from django.db import models 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils import timezone
import uuid

class UserRole(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, blank=False, unique=True)
    created_on = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

class CandidateMenter(models.Model):
    candidate=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='candidate')
    mentor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor')

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)