from rest_framework import generics

from . import models
from . import serializers
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from util import queries
from db_configs import db_default

# this method will return the sined in user details,
class UserListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # executing the native query
        user = User.objects.get(username=request.user.username)
        db_obj = db_default.VoiceTVInstance()
        user_details = db_obj.execute_related_query(queries.GET_CURRENT_USER, [request.user.username])[0]
        # deleting object
        del db_obj
        return Response(user_details)

# this method will return the mentor deatils with are maped with candidates,
class MentorCandiatesListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # executing the native query
        user = User.objects.get(username=request.user.username)
        db_obj = db_default.VoiceTVInstance()
        user_details = db_obj.execute_related_query(queries.GET_CURRENT_USER, [request.user.username])[0]
 
        candidate_details = []
        if user_details['role'] == "admin":
            candidate_details = db_obj.execute_related_query(queries.GET_TEAM_CANDIDATES, [])
        else :
            candidate_details = db_obj.execute_related_query(queries.GET_MENTOR_CANDIDATES, [user_details['id']])
        # deleting object
        del db_obj

        return Response(candidate_details)

