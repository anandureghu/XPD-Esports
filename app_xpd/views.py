from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import Announcement, Member, Lineup

# Create your views here.
def home(request):
    announcements = Announcement.objects.all()[::-1]
    members = Member.objects.all()
    lineups = Lineup.objects.all()
    return render(request, 'home.html', {"announcements": announcements, "members": members, "lineups": lineups})