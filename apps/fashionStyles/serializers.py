from apps.profiles.serializers import CategorySerializer
from .models import FashionInspo, FashionInspoImage, Styles, Category, Comment

from rest_framework import serializers

class FashionInspoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionInspoImage
        fields = ['id', 'front_image', 'back_image', 'caption']

class StylesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Styles
        fields = ['id', 'title', 'category', 'style_image']


class FashionInspoSerializer(serializers.ModelSerializer):
    images = FashionInspoImageSerializer(many=True, read_only=True)
    styles = StylesSerializer()
    likes_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = FashionInspo
        fields = ['id', 'title', 'description', 'styles', 'images', 'tags', 'likes_count', 'average_rating']