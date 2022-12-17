from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets, permissions
from rest_framework.decorators import action

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import UserPermission
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    serializer_class = AdSerializer
    serializers_by_action = {
        "create": AdDetailSerializer,
        "retrieve": AdDetailSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializers_by_action[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @property
    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
        elif self.action in ["retrieve", "create", "me", "partial_update", "destroy"]:
            self.permission_classes = [permissions.IsAuthenticated, UserPermission]
        else:
            self.permission_classes = [permissions.IsAdminUser, ]
        return super().get_permissions

    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.method == "GET":
            return Comment.objects.filter(ad_id=self.kwargs["ad_pk"])
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad_id=self.kwargs["ad_pk"])

    @property
    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
        elif self.action in ["retrieve", "create", "me", "partial_update", "destroy"]:
            self.permission_classes = [permissions.IsAuthenticated, UserPermission]
        else:
            self.permission_classes = [permissions.IsAdminUser, ]
        return super().get_permissions