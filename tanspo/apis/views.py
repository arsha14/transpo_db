from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apis.serializers import SurveySerializer, InterviewerSerializer, QuestionaireSerializer
from apis.models import Interviewer, Questionaire
from django.http import Http404

# Create your views here.

class Login(APIView):
	def post(self, request, format=None):
		info = request.data
		try:
			interviewer = Interviewer.objects.get(username=info['username'])
		except Interviewer.DoesNotExist:
			raise Http404
		if (info['password']==interviewer.password):
			serializer = InterviewerSerializer(interviewer)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			raise Http404

class Submit(APIView):
	def post(self, request, format=None):
		info = request.data
		info['interviewer']=Interviewer.objects.get(id=info['interviewer_id']).id
		serializer = SurveySerializer(data=info)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
