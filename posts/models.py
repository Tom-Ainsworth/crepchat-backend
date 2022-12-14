# External
from django.db import models

# Internal
from profiles.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    CATEGORY_CHOICES = [
        ("Adidas", "Adidas"),
        ("New Balance", "New Balance"),
        ("Nike", "Nike"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", default="../default_post_q8rncs.jpg", blank=True
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.caption}"
