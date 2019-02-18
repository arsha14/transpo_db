from rest_framework import serializers
from apis.models import Survey

class SurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = Survey
		fields = "__all__"