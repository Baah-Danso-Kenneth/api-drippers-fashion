from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer, UpdateProfileSerializer
from .renderers import ProfileJSONRenderer
from .exceptions import ProfileNotFound, NotYourProfile

class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def retrieve(self, request, pk=None):
        user = request.user
        try:
            user_profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            raise ProfileNotFound
        
        serializer = ProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'])
    def update_profile(self, request, pk=None):
        username = pk  # We will use pk to represent the username
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        if request.user.username != username:
            raise NotYourProfile

        data = request.data
        serializer = UpdateProfileSerializer(
            instance=request.user.profile, data=data, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
