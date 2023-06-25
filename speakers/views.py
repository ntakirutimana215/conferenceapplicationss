from django.shortcuts import render, get_object_or_404, redirect
from .models import Speaker
from .forms import SpeakerForm

def speaker_list(request):
    speakers = Speaker.objects.all()
    return render(request, 'speaker_list.html', {'speakers': speakers})

def speaker_detail(request, pk):
    speaker = get_object_or_404(Speaker, pk=pk)
    return render(request, 'speaker_detail.html', {'speaker': speaker})

def speaker_create(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES)
        if form.is_valid():
            speaker = form.save()
            return redirect('speaker_detail', pk=speaker.pk)
    else:
        form = SpeakerForm()
    return render(request, 'speaker_create.html', {'form': form})

def speaker_edit(request, pk):
    speaker = get_object_or_404(Speaker, pk=pk)
    if request.method == 'POST':
        form = SpeakerForm(request.POST, request.FILES, instance=speaker)
        if form.is_valid():
            speaker = form.save()
            return redirect('speaker_detail', pk=speaker.pk)
    else:
        form = SpeakerForm(instance=speaker)
    return render(request, 'speaker_edit.html', {'form': form})

def speaker_delete(request, pk):
    speaker = get_object_or_404(Speaker, pk=pk)
    if request.method == 'POST':
        speaker.delete()
        return redirect('speaker_list')
    return render(request, 'speaker_delete.html', {'speaker': speaker})
