from django.contrib import admin
from .models import Brand, Model, CarAnnouncement


admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(CarAnnouncement)