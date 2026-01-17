
from django.urls import include, path
from .views import getJobDetail

urlpatterns = [
    path("jobs/", getJobDetail, name="recent_jobs"),

]
