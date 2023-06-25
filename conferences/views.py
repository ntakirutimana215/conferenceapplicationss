from django.shortcuts import render, get_object_or_404, redirect
from .models import Conference
from .forms import ConferenceForm,SessionForm
from .models import  Session, Attendee, SessionReminder, Rating
def conference_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conference_list.html', {'conferences': conferences})

def conference_detail(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    return render(request, 'conference_detail.html', {'conference': conference})

def conference_create(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            conference = form.save()
            return redirect('conference_detail', pk=conference.pk)
    else:
        form = ConferenceForm()
    return render(request, 'conference_create.html', {'form': form})

def conference_edit(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    if request.method == 'POST':
        form = ConferenceForm(request.POST, instance=conference)
        if form.is_valid():
            conference = form.save()
            return redirect('conference_detail', pk=conference.pk)
    else:
        form = ConferenceForm(instance=conference)
    return render(request, 'conference_edit.html', {'form': form})

def conference_delete(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    if request.method == 'POST':
        conference.delete()
        return redirect('conference_list')
    return render(request, 'conference_delete.html', {'conference': conference})

def conference_schedule(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    return render(request, 'conference_schedule.html', {'conference': conference})



def conference_schedule(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    sessions = Session.objects.filter(conference=conference)
    return render(request, 'conference_schedule.html', {'conference': conference, 'sessions': sessions})

def attendee_registration(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        selected_sessions = request.POST.getlist('selected_sessions')
        payment_made = 'payment' in request.POST
        attendee = Attendee.objects.create(
            conference=conference,
            name=name,
            email=email,
            payment_made=payment_made
        )
        attendee.selected_sessions.set(selected_sessions)
        return redirect('conference_detail', pk=conference.pk)
    else:
        sessions = Session.objects.filter(conference=conference)
        return render(request, 'attendee_registration.html', {'conference': conference, 'sessions': sessions})

def session_create(request, conference_pk):
    conference = get_object_or_404(Conference, pk=conference_pk)
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.conference = conference
            session.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('conference_schedule', pk=conference.pk)
    else:
        form = SessionForm()
    return render(request, 'session_create.html', {'form': form, 'conference': conference})


def send_session_reminders(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    attendees = Attendee.objects.filter(conference=conference)
    for attendee in attendees:
        selected_sessions = attendee.selected_sessions.all()
        for session in selected_sessions:
            SessionReminder.objects.create(attendee=attendee, session=session)
    return redirect('conference_detail', pk=conference.pk)

def generate_reports(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    # Generate reports and perform analytics
    # ...
    return redirect('conference_detail', pk=conference.pk)



def session_detail(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    return render(request, 'sessions/session_detail.html', {'session': session})

def attendee_detail(request, attendee_id):
    attendee = get_object_or_404(Attendee, id=attendee_id)
    return render(request, 'sessions/attendee_detail.html', {'attendee': attendee})

def session_reminder_detail(request, session_reminder_id):
    session_reminder = get_object_or_404(SessionReminder, id=session_reminder_id)
    return render(request, 'sessions/session_reminder_detail.html', {'session_reminder': session_reminder})

def rating_detail(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    return render(request, 'sessions/rating_detail.html', {'rating': rating})
