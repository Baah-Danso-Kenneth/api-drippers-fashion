from rest_framework import routers
from apps.profiles.viewsets import ProfileViewSet


router = routers.SimpleRouter()
router.register(r'v1/profile', ProfileViewSet, basename='profile')

urlpatterns = router.urls