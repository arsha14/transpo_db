from django.contrib import admin
from apis.models import Survey
# Register your models here.
class SurveyAdmin(admin.ModelAdmin):
	list_display=('name', 'phone', 'gender', 'home', 'work')

admin.site.register(Survey, SurveyAdmin)