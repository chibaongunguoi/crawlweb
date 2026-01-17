from django.http import HttpResponse
from django.shortcuts import render

from .models import JobDetail

def index(request):
    return HttpResponse("Hello, world. You're at the application index.")

def recent_jobs(request):
    jobs = JobDetail.objects.order_by("-collected_at")[:5]
    return render(request, "api/recent_jobs.html", {"jobs": jobs})