from django.urls import path
from . import views
#important urls
urlpatterns = [
    path('', views.conference_list, name='conference_list'),
    path('create/', views.conference_create, name='conference_create'),
    path('<int:pk>/', views.conference_detail, name='conference_detail'),
    path('<int:pk>/edit/', views.conference_edit, name='conference_edit'),
    path('<int:pk>/delete/', views.conference_delete, name='conference_delete'),
    path('<int:pk>/schedule/', views.conference_schedule, name='conference_schedule'),
     path('<int:pk>/schedule/', views.conference_schedule, name='conference_schedule'),
    path('<int:conference_pk>/sessions/create/', views.session_create, name='session_create'),
    path('<int:pk>/register/', views.attendee_registration, name='attendee_registration'),
    path('<int:pk>/send_reminders/', views.send_session_reminders, name='send_session_reminders'),
    path('<int:pk>/generate_reports/', views.generate_reports, name='generate_reports'),
    path('sessions/<int:session_id>/', views.session_detail, name='session_detail'),
    path('attendees/<int:attendee_id>/', views.attendee_detail, name='attendee_detail'),
    path('session-reminders/<int:session_reminder_id>/', views.session_reminder_detail, name='session_reminder_detail'),
    path('ratings/<int:rating_id>/', views.rating_detail, name='rating_detail'),
]