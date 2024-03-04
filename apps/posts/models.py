from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=255)
    title = models.TextField()
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_datetime"]

    def __str__(self) -> str:
        return f"{self.username}'s {self.id}º post"
