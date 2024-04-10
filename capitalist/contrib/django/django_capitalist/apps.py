from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class DjangoCapitalistConfig(AppConfig):
    name = 'capitalist.contrib.django.django_capitalist'
    verbose_name = _('Capitalist')
