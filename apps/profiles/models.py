from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from apps.sharedApps import TimeStampedModel

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="category_images/")

    def __str__(self):
        return self.name

class Profile(TimeStampedModel):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name =_("Phone Number"), max_length=30, default="+233 8603555"
    )
    about_me = models.TextField(
        verbose_name=_("About me"), default="Say something about your self"
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"),
        default="/profile_photo.png"
    )

    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    country = CountryField(
        verbose_name=_("Country"),
        default="GH",
        blank=False,
        null=False
    )

    subscribed = models.BooleanField(
        verbose_name=_("Subscribed"),
        default=False,
        help_text=_("Upgraded user")
    )
    
    def __str__(self):
        return f"{self.user.username}'s profile"