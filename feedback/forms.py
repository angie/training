from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from feedback.models import Attendee, Company, Role

class AttendeeForm(forms.ModelForm):

	first_name = forms.CharField(max_length=25)
	last_name  = forms.CharField(max_length=25)
	
	# Foreign keys
	
	company = forms.ModelChoiceField(
		queryset = Company.objects.all(),
		label = 'Company Name'
	)
	
	role = forms.ModelChoiceField(
		queryset = Role.objects.all(),
		label = 'Job Role'
	)
	
	# -- End foreign keys
	
	email = forms.EmailField(max_length=45)
	phone_number = forms.CharField(max_length=20)
	
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	EXPERIENCE_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No'),
	)
	sex = forms.ChoiceField(choices=GENDER_CHOICES)
	experience = forms.ChoiceField(
		label = 'Previous experience?',
		widget = forms.RadioSelect(),
		choices = EXPERIENCE_CHOICES)
	
	# Crispy forms section
	def __init__(self, *args, **kwargs):
		super(AttendeeForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-attendeeForm'
		self.helper.form_class = ''
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_survey'
		
		self.helper.add_input(Submit('submit', 'Continue'))
	
	class Meta:
		model = Attendee
		fields = ['first_name', 
				  'last_name', 
				  'email',
				  'phone_number', 
				  'sex', 
				  'experience',
				  'company',
				  'role']
				  
class FeedbackForm(forms.ModelForm):
	pass		  