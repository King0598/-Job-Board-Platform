from rest_framework import generics, permissions
from .models import EmployerProfile
from .serializers import EmployerProfileSerializer
from src.modules.common.permissions import IsEmployer

class EmployerProfileView(generics.RetrieveUpdateAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def get_object(self):
        return self.request.user.employer_profile