from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from feedback.models import AnswerOffered, Attendee, Question
from feedback.forms import AttendeeForm, FeedbackForm, QuestionForm
from django.utils.timezone import now

# View helper functions
def get_offered_answers():
	answers = AnswerOffered.objects.all()
	return answers

def get_questions():
	questions = Question.objects.all()
	return questions

# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {}
		
	return render_to_response('feedback/index.html', context_dict, context)
	
def add_attendee(request):
	context = RequestContext(request)
	context_dict = {}
	
	if request.method == 'POST':
		attendee_form = AttendeeForm(request.POST)
		# check form is valid then save to DB
		if attendee_form.is_valid():
			attendee_obj = attendee_form.save(commit=False)
			attendee_obj.save()
			context_dict['attendee'] = attendee_obj
			# redirect to questions page and pass ID of new attendee
			return HttpResponseRedirect('/feedback/questions/%s/' % attendee_obj.attendee_id)
		else:
			return HttpResponse(attendee_form.errors)
	else:
		a_form = AttendeeForm()
	
	context_dict['a_form'] = a_form
	return render_to_response('feedback/add_attendee.html', context_dict, context)
	

def feedback_form(request):
	context = RequestContext(request)
	context_dict = {}
		
	return render_to_response('feedback/feedback_form.html', context_dict, context)
	
def new_form(request, attendee_id):

	context = RequestContext(request)
	context_dict = {}
	a = get_object_or_404(Attendee, pk=attendee_id) # grab new attendee 
	# set up context_dict with required objects
	q_form = QuestionForm()
	context_dict['q_form'] = q_form
	context_dict['attendee'] = a
	context_dict['questions'] = get_questions()
	context_dict['offered_answers'] = get_offered_answers()
	
	# displaying the form
	if request.method == 'POST':
		feedback_form = FeedbackForm(request.POST)
		if feedback_form.is_valid():
			feedback_obj = feedback_form.save(commit=False)
			# save against the attendee
			feedback_obj.attendee = a
			feedback_obj.save()
			context_dict['feedback_form'] = feedback_obj
			# display form
			return HttpResponseRedirect('/feedback/')
		else:
			return HttpResponse(feedback_form.errors)
	else:
		f_form = FeedbackForm()
	context_dict['f_form'] = f_form
	
	return render_to_response('feedback/questions.html', context_dict, context)
