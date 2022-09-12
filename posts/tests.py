from profiles.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="tom", password="password")

    def test_can_list_posts(self):
        tom = User.objects.get(username="tom")
        Post.objects.create(owner=tom, caption="caption")
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username="tom", password="password")
        response = self.client.post("/posts/", {"caption": "caption"})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_post(self):
        response = self.client.post("/posts/", {"caption": "caption"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        tom = User.objects.create_user(username="tom", password="password")
        ellie = User.objects.create_user(username="ellie", password="password")

        Post.objects.create(owner=tom, caption="toms post")
        Post.objects.create(owner=ellie, caption="ellies post")

    def test_user_can_retrieve_post_with_valid_id(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.data["caption"], "toms post")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_retrieve_post_with_invalid_id(self):
        response = self.client.get("/posts/1000/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_users_can_update_posts_they_own(self):
        self.client.login(username="tom", password="password")
        response = self.client.put("/posts/1/", {"caption": "updated caption!"})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.caption, "updated caption!")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_cant_update_posts_they_dont_own(self):
        self.client.login(username="ellie", password="password")
        response = self.client.put("/posts/1/", {"caption": "updated caption!"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
