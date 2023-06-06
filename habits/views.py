from django.shortcuts import render, redirect, get_object_or_404
from .models import Tracker, User
from .forms import TrackerForm
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


def create_tracker(request):
    if request.method == "GET":
        form = TrackerForm()

    else:
        form = TrackerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'habits/user_info.html')
    return render(request, 'habits/create_tracker.html', {'form': form})


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
    return redirect('user-info', pk=pk)
