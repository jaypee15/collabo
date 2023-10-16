from django.contrib.auth.models import AbstractUser
from django.db.models import (CharField, EmailField, TextField, 
                              ManyToManyField, BooleanField)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from collabo.users.managers import UserManager
from collabo.projects.models import Skill


class User(AbstractUser):
    """
    Default custom user model for collabo.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = CharField(_("Username of User"), max_length=100, blank=True)
    bio = TextField(_("user bio"), blank=True)
    website = TextField(_("link to user's personal website"), blank=True)
    twitter = CharField(_("link to user's twitter profile"), max_length=100, blank=True)
    linkedin = CharField(_("link to user's linkedin url"), max_length=100, blank=True)
    skills = ManyToManyField( Skill, related_name="user_skills", blank=True, verbose_name=_("user's skills"))
    is_open_to_collab = BooleanField(_("user is open to collaboration"), default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


