from django.contrib import admin
from apis.models import Survey, Interviewer, Questionaire
# Register your models here.
class SurveyAdmin(admin.ModelAdmin):
	list_display=('name', 'phone', 'gender', 'home', 'work')

class QuestionsInline(admin.TabularInline):
	model=Interviewer.questions.through
	verbose_name = u"Question"
	verbose_name_plural = u"Questions"
	extra=0

class InterviewerAdmin(admin.ModelAdmin):
	inlines = (
		QuestionsInline,
	)
	list_display=('username', 'password')

class QuestionaireAdmin(admin.ModelAdmin):
	list_display=('question', 'question_name')

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Interviewer, InterviewerAdmin)
admin.site.register(Questionaire, QuestionaireAdmin)