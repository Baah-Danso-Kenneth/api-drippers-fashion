from rest_framework import routers
from apps.profiles.viewsets import ProfileViewSet, CategoryViewSet


router = routers.SimpleRouter()
router.register(r'v1/profile', ProfileViewSet, basename='profile')
router.register(r'v1/categories', CategoryViewSet, basename='category')

urlpatterns = router.urls