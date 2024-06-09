from rest_framework import serializers
from .models import FashionInspo, FashionInspoImage, Styles, Category, Comment


class FashionInspoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionInspoImage
        fields = ['id', 'front_image', 'back_image', 'caption']

class StylesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Styles
        fields = ['id', 'title', 'category', 'style_image']


class FashionInspoSerializer(serializers.ModelSerializer):
    images = FashionInspoImageSerializer(many=True, read_only=True)
    styles = StylesSerializer(read_only=True)
    likes_count = serializers.ReadOnlyField(source='likes_count')
    average_rating = serializers.ReadOnlyField(source='average_rating')

    class Meta:
        model = FashionInspo
        fields = ['id', 'title', 'description', 'styles', 'images', 'tags', 'source', 'likes_count', 'average_rating']
