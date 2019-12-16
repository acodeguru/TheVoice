from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from authentication.models import UserProfile, UserRole, CandidateMenter
from performance.models import Performance,PerformanceScore
from util import song_list, modifier, name_list
import random
import datetime

class Command(BaseCommand):
    help = 'Create random users'
    userroles = ["admin", "candidate", "mentor"]
    
    def add_arguments(self, parser):
        parser.add_argument('admins', type=int, help='Indicates the number of admins to be created')
        parser.add_argument('mentors', type=int, help='Indicates the number of mentors to be created')
        parser.add_argument('candidates', type=int, help='Indicates the number of candidates to be created')

    def handle(self, *args, **kwargs):

        User.objects.exclude(id=1).all().delete()
        UserRole.objects.all().delete()

        for userrole in self.userroles:
            UserRole.objects.create(name=userrole)

        admins = kwargs['admins']
        mentors = kwargs['mentors']
        candidates = kwargs['candidates']

        for index in range(admins):
                
            random_role = "admin"
            random_first_name = random.choice(name_list.NAME_LIST)
            random_last_name = random.choice(name_list.NAME_LIST)
            random_username = get_random_string()+"@.demoexample.com"
            user  = User.objects.create_user(username=random_username, email=random_username,first_name=random_first_name, last_name=random_last_name, password='123',is_active=True)
            UserProfile.objects.create(user=user,role=UserRole.objects.get(name=random_role))
            print("created '",random_username, "' with password '123' as a '",random_role,"'")

        for index in range(mentors):
     
            random_role = "mentor"
            random_first_name = random.choice(name_list.NAME_LIST)
            random_last_name = random.choice(name_list.NAME_LIST)
            random_username = get_random_string()+"@.demoexample.com"
            user  = User.objects.create_user(username=random_username, email=random_username,first_name=random_first_name, last_name=random_last_name, password='123',is_active=True)
            UserProfile.objects.create(user=user,role=UserRole.objects.get(name=random_role))
            print("created '",random_username, "' with password '123' as a '",random_role,"'")
 
        for index in range(candidates):
            random_role = "candidate"
            random_first_name = random.choice(name_list.NAME_LIST)
            random_last_name = random.choice(name_list.NAME_LIST)
            random_username = get_random_string()+"@.demoexample.com"
            user  = User.objects.create_user(username=random_username, email=random_username,first_name=random_first_name, last_name=random_last_name, password='123',is_active=False)
            UserProfile.objects.create(user=user,role=UserRole.objects.get(name=random_role))
            print("created '",random_username, "' with password '123' as a '",random_role,"'")

        all_mentors = User.objects.filter(userprofile__role=UserRole.objects.get(name="mentor"))
        all_candidates = User.objects.filter(userprofile__role=UserRole.objects.get(name="candidate"))

        for candidate in all_candidates:  
            random_mentor =all_mentors[random.randint(0, len(all_mentors)-1)]
            print(str(candidate), str(random_mentor))
            CandidateMenter.objects.create(candidate=candidate, mentor=random_mentor)

            random_song = random.choice(song_list.SONG_LIST)
            random_day = random.randint(0, 30)
            random_date = modifier.random_date("2019-11-01", random_day)

            performance = Performance.objects.create(candidate=candidate,song_name=random_song,event_date=random_date)

            for mentor in all_mentors:
                random_score = random.randint(0, 100)
                PerformanceScore.objects.create(performance=performance,mentor=mentor,score=random_score)





