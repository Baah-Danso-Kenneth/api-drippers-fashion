from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Profile
from .serializers import CategorySerializer, ProfileSerializer, UpdateProfileSerializer
from .exceptions import ProfileNotFound, NotYourProfile


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def retrieve(self, request, pk=None):
        user = request.user
        try:
            user_profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        serializer = ProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['patch'], url_path='update-profile')
    def update_profile(self, request):
        user = request.user
        try:
            user_profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        data = request.data
        serializer = UpdateProfileSerializer(
            instance=user_profile, data=data, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        category = serializer.data.get('category').lower()
        if category == 'male':
            redirect_url = '/men-page'
        elif category == 'female':
            redirect_url = '/women-page'
        elif category == 'kids':
            redirect_url = '/kids-page'
        else:
            redirect_url = '/other-page'

        return Response({"profile": serializer.data, "redirect_url": redirect_url}, status=status.HTTP_200_OK)
