# External
from django.urls import path

# Internal
from followers import views

urlpatterns = [
    path("followers/", views.FollowerList.as_view()),
    path("followers/<int:pk>/", views.FollowerDetail.as_view()),
]
