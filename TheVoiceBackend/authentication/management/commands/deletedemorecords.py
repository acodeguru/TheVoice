from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from authentication.models import UserProfile, UserRole, CandidateMenter
from performance.models import Performance
from django.db.models import Q
import util
import random

class Command(BaseCommand):
    help = 'Remove all users without super user'
    
    def handle(self, *args, **kwargs):

        User.objects.exclude(id=1).all().delete()




