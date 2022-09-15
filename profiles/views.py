# External
from rest_framework import generics, filters
from django.db.models import Count

# Internal
from .models import Profile
from .serializers import ProfileSerializer
from CrepChat.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """Generic list view for all profiles. Profile creation is handled by django signals from the user instance, so no need for a create view"""

    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count("owner__post", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        "posts_count",
        "followers_count",
        "following_count",
        "owner__following__created_at",
        "owner__followed__created_at",
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """Generic view to update and delete a profile."""

    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Profile.objects.annotate(
        posts_count=Count("owner__post", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
