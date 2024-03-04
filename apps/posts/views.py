from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.posts.models import Post
from apps.posts.pagination import PostPagination
from apps.posts.serializers import PostSerializer, UpdatePostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"
    pagination_class = PostPagination

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UpdatePostSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(PostSerializer(instance).data, status=status.HTTP_200_OK)
