from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    first_name = models.CharField('First name of the user', blank=True, max_length=20)
    last_name = models.CharField('Last name of the user', blank=True, max_length=20)

    # define the custom permissions
    class Meta:
        permissions = (
            ('can_go_in on AC bus', 'To provide non AC bus facility'),
            ('can_go_in_ac_bus', 'To provide AC-Bus facility'),
            ('can_stay_ac-room', 'To provide staying at AC room'),
            ('cant_stay_ac-room', 'To provide staying at Non-AC room'),
            ('can_go_dehradoon', 'Trip to Dehradoon'),
            ('can_go_mussoorie', 'Trip to Mussoorie'),
            ('can_go_haridwaar', 'Trip to Haridwaar'),
            ('can_go_rishikesh', 'Trip to Rishikesh'),
        )
