from rest_framework import serializers

from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "content")
