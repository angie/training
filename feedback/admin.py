from django.contrib import admin
from feedback.models import Attendee, AnswerOffered, Company, Form, Question, Role, TrainingType
from feedback.forms import AttendeeForm


class TrainingTypeAdmin(admin.ModelAdmin):
	pass
	
class AnswerOfferedAdmin(admin.ModelAdmin):
	list_display = ('answer_offered_id', 'answer_text')
	ordering = ('answer_offered_id',)
	fields = ['answer_text']
	
class AttendeeAdmin(admin.ModelAdmin):
	list_display = ('first_name',
				 	'last_name',
				 	'company',
				 	'role',
				 	'created')
				 	
	fields = ['first_name', 
			  'last_name', 
			  'email',
			  'phone_number', 
			  'sex', 
			  'experience',
			  'company',
			  'role']		 	
	#form = AttendeeForm
				 	
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name', 'industry', 'postcode')
	
class FormAdmin(admin.ModelAdmin):
	fields = ['attendee', 'training_type', 'date']
	
class QuestionAdmin(admin.ModelAdmin):
	fields = ['question']

# Register your models here.
admin.site.register(AnswerOffered, AnswerOfferedAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Role)
admin.site.register(TrainingType)
