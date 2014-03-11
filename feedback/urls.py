from django.conf.urls import patterns, url
from feedback import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_attendee/', views.add_attendee, name='add_attendee'),
    url(r'^add_feedback/', views.feedback_form, name='feedback_form'),
    url(r'^questions/(?P<attendee_id>\d+)/', views.new_form, name='new_form'),
)
