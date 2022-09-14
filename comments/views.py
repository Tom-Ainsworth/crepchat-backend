# External
from rest_framework import generics, permissions

# Internal
from CrepChat.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """Generic list view for comments"""

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Generic detail view for comment owner to perform actions on their comments"""

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
