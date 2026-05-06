from rest_framework import serializers
from .models import Application
from src.modules.job.serializers import JobSerializer
from src.modules.candidate.serializers import CandidateProfileSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)
    candidate_name = serializers.CharField(source='candidate.full_name', read_only=True)

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['candidate', 'applied_at', 'updated_at']

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['job', 'cover_letter']

    def validate(self, data):
        user = self.context['request'].user
        if user.role != 'candidate':
            raise serializers.ValidationError("Only candidates can apply.")
        if data['job'].status != 'open':
            raise serializers.ValidationError("This job is no longer accepting applications.")
        if Application.objects.filter(job=data['job'], candidate=user.candidate_profile).exists():
            raise serializers.ValidationError("You have already applied for this job.")
        return data