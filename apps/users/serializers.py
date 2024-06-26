from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="profile.category")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ImageField(source="profile.profile_photo")
    country = CountryField(source="profile.country")
    subscribed = serializers.BooleanField(source="profile.subscribed")
    frst_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(source="profile.full_name")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "category",
            "phone_number",
        ]

    def get_first_name(self, obj):
        return obj.first_name
    
    def get_last_name(self, obj):
        return obj.last_name
    
    def to_representation(self, instance):
        representation = super(UserSerializer).to_representation(instance)
        if instance.is_superuser:
            representation['admin'] = True
        return representation
    

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
    
