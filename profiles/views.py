# External
from rest_framework import generics

# Internal
from .models import Profile
from .serializers import ProfileSerializer
from CrepChat.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """Generic list view for all profiles. Profile creation is handled by django signals from the user instance, so no need for a create view"""

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """Generic view to update and delete a profile."""

    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
