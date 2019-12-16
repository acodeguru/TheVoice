from rest_framework import generics

from . import models
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from util import queries
from db_configs import db_default

# this method will return the candidates scores,
# to fetch the data it will take candidate id
class CandiateMentorScoreListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        # fetching the signed in user details
        user = User.objects.get(username=request.user.username)
        db_obj = db_default.VoiceTVInstance()
        user_details = db_obj.execute_related_query(queries.GET_CURRENT_USER, [request.user.username])[0]
        candidate_details = {}
        if user_details['role'] == "admin":
            # executing the native query
            candidate_details = db_obj.execute_related_query(queries.GET_CANDIDATE_SCORE, [pk])

        else :
            candidate_details['candidate_detail'] = db_obj.execute_related_query(queries.GET_MENTOR_CANDIDATE_SCORE, [pk])
            candidate_details['mentor_avgscore'] = db_obj.execute_related_query(queries.GET_MENTOR_AVG_SCORE, [user_details['id']])[0]

        # deleting object
        del db_obj

        return Response(candidate_details)
