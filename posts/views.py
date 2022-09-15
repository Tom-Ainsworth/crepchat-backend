# External
from rest_framework import permissions, generics, filters
from django.db.models import Count

# Internal
from .models import Post
from .serializers import PostSerializer
from CrepChat.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """Generic view to list and create posts"""

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count("comment", distinct=True),
        likes_count=Count("likes", distinct=True),
        dislikes_count=Count("dislikes", distinct=True),
    ).order_by("-created_at")
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        "comments_count",
        "likes_count",
        "dislikes_count",
        "likes__created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Generic view to read, update and delete posts"""

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count("comment"),
        likes_count=Count("likes"),
        dislikes_count=Count("dislikes"),
    ).order_by("-created_at")
