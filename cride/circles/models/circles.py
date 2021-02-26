"""Circle models."""

# Django
from django.db import models

# Utilities
from cride.utils.models import  CRideModel

class Circle(CRideModel):
    """Circle models.
    A circles is private group where rides are offered and taken
    by its members, to join a circle a user must recive an unique
    invitation code from an existing circle member.
    """


    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circle/pictures', blank=True, null=True)

    # status
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circles',
        default=False,
        help_text='Verified circles are also as official communities'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='public circles are listed in page so every know about their existence.'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members'
    )

    members_limit = models.PositiveIntegerField(
    default=0,
    help_text=' If circles is limited, this will be the limit on the number of members'
    )

    def __str__(self):
        """Return circle name."""
        return self.name

    class Meta(CRideModel.Meta):
            """Meta class."""

            ordering =['-rides_taken', '-rides_offered']