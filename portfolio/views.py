from django.shortcuts import render
from jobs.models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'home.html', {'jobs': jobs})