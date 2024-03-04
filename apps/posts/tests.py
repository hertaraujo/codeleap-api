from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase

from apps.posts.models import Post


class TestPosts(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("/posts", include("apps.posts.urls")),
    ]

    def setUp(self):
        self.credentials = {
            "email": "testuser",
            "password": "testpass",
        }

        self.post = Post.objects.create(
            username="John Doe",
            title="test title",
            content="test contet",
        )

    def test_list_posts(self):
        url = reverse("post-list")

        resp = self.client.get(
            url,
        )

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("count"), 1)

    def test_create_post(self):
        url = reverse("post-list")
        payload = {
            "username": "test-username",
            "title": "test-title",
            "content": "test-content",
        }
        resp = self.client.post(url, payload)

        data = resp.json()
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data.get("username"), "test-username")
        self.assertEqual(data.get("title"), "test-title")
        self.assertEqual(data.get("content"), "test-content")

    def test_get_by_id(self):
        url = reverse("post-details", kwargs={"id": self.post.id})

        resp = self.client.get(url)

        data = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data.get("username"), self.post.username)
        self.assertEqual(data.get("title"), self.post.title)
        self.assertEqual(data.get("content"), self.post.content)

    def test_update_post(self):
        url = reverse("post-details", kwargs={"id": self.post.id})

        payload = {
            "username": "test-username",
            "title": "test-title",
            "content": "test-content",
        }
        resp = self.client.patch(url, payload)

        data = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.post.refresh_from_db()
        self.assertNotEqual(payload.get("username"), self.post.username)
        self.assertEqual(data.get("title"), self.post.title)
        self.assertEqual(data.get("content"), self.post.content)

    def test_delete_post(self):
        url = reverse("post-details", kwargs={"id": self.post.id})

        resp = self.client.delete(url)

        self.assertEqual(resp.status_code, 204)

        url = reverse("post-details", kwargs={"id": self.post.id})

        resp = self.client.get(url)

        data = resp.json()
        self.assertEqual(data.get("detail"), "Not found.")
