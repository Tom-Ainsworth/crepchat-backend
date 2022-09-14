# External
from rest_framework import serializers
from django.db import IntegrityError

# Internal
from .models import Follower


class FollowerSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    followed_name = serializers.ReadOnlyField(source="followed.username")

    class Meta:
        model = Follower
        fields = ["id", "owner", "followed_name", "created_at", "followed"]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "possible duplicate"})