from rest_framework import serializers
from .models import JobDetail

class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetail
        fields = '__all__'