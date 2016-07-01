from django.contrib import admin
from .models import Question, Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['question_text']}),
		('Date information',{'fields':['pub_date']}),
		('Total Votes',{'fields':['total_votes']}),
		('Voted Users',{'fields':['voted_users']}),
	]
	inlines = [ChoiceInline]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
