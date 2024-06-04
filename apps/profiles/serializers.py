from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from apps.fashionStyles.models import Styles

from .models import Category, Profile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']

    def validate_name(self, value):
        return value.lower()

class StyleSerializer(serializers.ModelSerializer):
    category =CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    class Meta:
        model = Styles
        fields = ['title', 'category', 'category_id']

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.CharField(source="user.get_full_name")
    country = CountryField(name_only=True)
    category = CategorySerializer()

    class Meta:
        model = Profile
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "full_name",
            "country",
            "subscribed",
            "category",
            "profile_photo",
            "about_me",
            "phone_number",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.subscribed:
            representation["subscribed"] = True
        return representation
    

class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    full_name = serializers.CharField(source="user.get_full_name")

    class Meta:
        fields = [
            "phone_number",
            "profile_photo",
            "about_me",
            "category",
            "country",
            "phone_number",
            "full_name"
        ]
    
    
