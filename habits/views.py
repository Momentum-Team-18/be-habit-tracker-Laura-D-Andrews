from django.shortcuts import render, redirect, get_object_or_404
from .models import Tracker, User, Record
from .forms import TrackerForm, RecordForm
# Create your views here.


def index(request):
    return render(request, 'habits/index.html')


def user_info(request, pk):
    trackers = Tracker.objects.filter(user_id=pk)
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user,
        'trackers': trackers,
    }
    return render(request, 'habits/user_info.html', context)


def tracker_detail(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    return render(request, 'habits/tracker_details.html', {'tracker': tracker})


def create_tracker(request, user_pk):
    if request.method == "GET":
        form = TrackerForm()

    else:
        form = TrackerForm(request.POST)
        tracker = form.save(commit=False)
        tracker.user_id = user_pk
        tracker.save()
        return redirect('user-info', user_pk)
    return render(request, 'habits/create_tracker.html', {'form': form})


def add_goal_met_data(request, pk):
    if request.method == "GET":
        form = RecordForm()
    else:
        form = RecordForm(request.POST)
        record = form.save(commit=False)
        record.tracker_id = pk
        form.save()
        return redirect('tracker-detail', pk=pk)
    return render(request, 'habits/add_goal_met_data.html', {'form': form})


def edit_tracker(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    if request.method == "GET":
        form = TrackerForm(instance=tracker)

    else:
        form = TrackerForm(request.POST, instance=tracker)
        if form.is_valid():
            form.save()
            return redirect('tracker-detail', pk=pk)
    return render(request, 'habits/edit_tracker.html', {'form': form})


def delete_tracker(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    tracker.delete()
    return redirect('home')


def edit_submission(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "GET":
        form = TrackerForm(instance=record)

    else:
        form = TrackerForm(request.POST, instance=record)
        record = form.save(commit=False)
        record.tracker_id = pk
        form.save()
        return redirect('tracker-detail', pk=pk)
    return render(request, 'habits/edit_submission.html', {'form': form})


def delete_submission(request, pk):
    record = get_object_or_404(Record, pk=pk)
    record.delete()
    return redirect('home')
