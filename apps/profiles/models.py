from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from apps.sharedApps import TimeStampedModel

User = get_user_model()

class Category(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    KIDS = "Kids", _("Kids")
    OTHER = "Other", _("Other")


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

    category = models.CharField(
        verbose_name=_("Category"),
        choices=Category.choices,
        max_length=6,
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