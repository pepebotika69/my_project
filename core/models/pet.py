from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from core.models import Animal


class Pet(TimeStampedModel):
    name = models.CharField(_('Pet name'), max_length=255)
    animal = models.ForeignKey(Animal, related_name='animal', on_delete=models.PROTECT, null=True, blank=True)
    birthday = models.DateField(_('Birthday'), null=True, blank=True)
