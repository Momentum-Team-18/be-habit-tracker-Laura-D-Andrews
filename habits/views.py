from django.shortcuts import render, redirect, get_object_or_404
from .models import Tracker, User
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
