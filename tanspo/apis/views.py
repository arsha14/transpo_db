from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apis.serializers import SurveySerializer

# Create your views here.
class Submit(APIView):
	def post(self, request, format=None):
		info = request.data
		serializer = SurveySerializer(data=info)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
