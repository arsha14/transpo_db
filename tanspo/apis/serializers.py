from rest_framework import serializers
from apis.models import Survey, Questionaire, Interviewer

class InterviewerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Interviewer
		fields = "__all__"

class SurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = Survey
		fields = "__all__"
class QuestionaireSerializer(serializers.ModelSerializer):
	class Meta:
		model = Questionaire
		fields = "__all__" 