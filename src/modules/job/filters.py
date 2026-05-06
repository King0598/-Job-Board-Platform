import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')
    job_type = django_filters.ChoiceFilter(choices=Job.JobType.choices)
    salary_min = django_filters.NumberFilter(field_name='salary_min', lookup_expr='gte')
    salary_max = django_filters.NumberFilter(field_name='salary_max', lookup_expr='lte')
    skills_required = django_filters.CharFilter(method='filter_skills')

    def filter_skills(self, queryset, name, value):
        skills = value.split(',')
        q = models.Q()
        for skill in skills:
            q |= models.Q(skills_required__icontains=skill.strip())
        return queryset.filter(q)

    class Meta:
        model = Job
        fields = ['title', 'location', 'job_type', 'status', 'salary_min', 'salary_max', 'skills_required']