# External
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


# Internal
from .models import Post
from .serializers import PostSerializer
from CrepChat.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """Generic view to list and create posts"""

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Generic view to read, update and delete posts"""

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
