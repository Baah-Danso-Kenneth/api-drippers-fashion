from rest_framework import routers
from apps.fashionStyles.viewsets import StylesCategoryViewSet
from apps.profiles.viewsets import ProfileViewSet, CategoryViewSet


router = routers.SimpleRouter()
router.register(r'v1/profile', ProfileViewSet, basename='profile')
router.register(r'v1/categories', CategoryViewSet, basename='category')
router.register(r'v1/styles-category',StylesCategoryViewSet, basename='styles-category')

urlpatterns = router.urls