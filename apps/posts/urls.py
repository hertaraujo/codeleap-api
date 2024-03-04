from django.urls import path

from apps.posts.views import (
    PostViewSet,
)

urlpatterns = [
    path(
        "",
        PostViewSet.as_view({"get": "list", "post": "create"}),
        name="post-list",
    ),
    path(
        "<str:id>",
        PostViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="post-details",
    ),
]
