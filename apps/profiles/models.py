from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE,
    )
    about_me = models.TextField(
        verbose_name=_("About me"),
        default="say something about yourself",
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"),
        upload_to="media",
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("Country"),
        default="GH",
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.user.username}'s profile"