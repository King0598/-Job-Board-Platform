from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('src.modules.auth.urls')),
    path('api/users/', include('src.modules.user.urls')),
    path('api/employers/', include('src.modules.employer.urls')),
    path('api/candidates/', include('src.modules.candidate.urls')),
    path('api/jobs/', include('src.modules.job.urls')),
    path('api/applications/', include('src.modules.application.urls')),
    path('api/resumes/', include('src.modules.resume.urls')),
    path('api/reports/', include('src.modules.report.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)