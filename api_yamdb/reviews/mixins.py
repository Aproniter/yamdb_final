from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet

from api.permissions import IsAdminOrReadOnly


class CreateDestroyListMixinSet(
    CreateModelMixin, ListModelMixin,
    DestroyModelMixin, GenericViewSet
):
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class CreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass
