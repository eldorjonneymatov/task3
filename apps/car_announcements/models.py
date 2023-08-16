from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel

class Brand(BaseModel):
    name = models.CharField(_('Name'), max_length=40)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.name
    

class Model(BaseModel):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='models',
        verbose_name=_('Brand')
    )
    name = models.CharField(_('Name'), max_length=40)

    class Meta:
        verbose_name = _('Model')
        verbose_name_plural = _('Models')

    def __str__(self):
        return self.name
    

class CarAnnouncement(BaseModel):
    model = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        related_name='announcements',
        verbose_name=_('Model')
    )
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=16)

    class Meta:
        verbose_name = _('CarAnnouncement')
        verbose_name_plural = _('CarAnnouncements')

    def __str__(self):
        return f"{self.model.name} {self.price}"