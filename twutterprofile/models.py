from django.db import models
from django.contrib.auth.models import User


class TwutterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)  # noqa


# Automatically creates a TwutterUser whenever a user is created.
# I picked this trick up from a friend I met at a meetup!
User.twutterprofile = property(
    lambda u: TwutterProfile.objects.get_or_create(user=u)[0]
    )
