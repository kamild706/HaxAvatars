from django.http import Http404
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from avatars.models import Avatar
from avatars.serializers import AvatarSerializer, AdminAvatarSerializer


class AvatarList(mixins.ListModelMixin, generics.GenericAPIView):
    """
    Listing available avatars
    """
    queryset = Avatar.objects.filter(is_deleted=False)  # show not deleted avatars only
    serializer_class = AvatarSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AdminAvatarList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    Listing and creating avatars
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = AdminAvatarSerializer

    def get(self, request, state, *args, **kwargs):
        deleted = True if state == 'deleted' else False  # state is passed through url
        self.queryset = Avatar.objects.filter(is_deleted=deleted)  # whether list deleted or not deleted avatars
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AvatarDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """
    Detail page about given avatar
    """
    serializer_class = AvatarSerializer

    def get(self, request, pk, *args, **kwargs):
        self.queryset = Avatar.objects.filter(pk=pk, is_deleted=False)  # show not deleted avatar only
        return self.retrieve(request, *args, **kwargs)


class AdminAvatarDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    """
    Detail and management page about given avatar
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = AdminAvatarSerializer
    queryset = Avatar.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk):
        try:
            avatar = Avatar.objects.get(pk=pk)
        except Avatar.DoesNotExist:
            raise Http404

        # We won't remove avatar from database
        # Instead we set its is_deleted attribute to True
        avatar.is_deleted = True
        avatar.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
