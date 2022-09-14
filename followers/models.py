from tkinter import CASCADE
from django.db import models
from profiles.models import User


class Follower(models.Model):
    """
    Follower model, related to 'owner' and 'followed'.
    'owner' is a User that is following a User (aka the follower).
    'followed' is another User that is followed by 'owner' (current user).
    The related_name attribute lets django differentiate between the two, and help avoid confusion.
    between 'owner/follower' and 'other user/followed user' who both are User model instances.
    'unique_together' makes sure a user can't 'double follow' the same user.
    """

    owner = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    followed = models.ForeignKey(
        User, related_name="followed", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["owner", "followed"]

    def __str__(self):
        return f"{self.owner} {self.followed}"
