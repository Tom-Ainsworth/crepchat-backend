from rest_framework import generics, permissions

# Internal
from CrepChat.permissions import IsOwnerOrReadOnly
from .models import Like, Dislike
from .serializers import LikeSerializer, DislikeSerializer


class LikeList(generics.ListCreateAPIView):
    """Generic list view for comments"""

    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """Generic view to retrive and delete likes. No need to update them"""

    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()


class DislikeList(generics.ListCreateAPIView):
    """Generic list view for comments"""

    serializer_class = DislikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Dislike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DislikeDetail(generics.RetrieveDestroyAPIView):
    """Generic view to retrive and delete Dislikes. No need to update them"""

    serializer_class = DislikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Dislike.objects.all()
