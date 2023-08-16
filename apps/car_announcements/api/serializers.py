from rest_framework import serializers
from django.db.models.aggregates import Avg
from apps.car_announcements.models import CarAnnouncement, Model


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('id', 'name', 'brand')


class CarAnnouncementSerializer(serializers.ModelSerializer):
    model = ModelSerializer()
    average_price = serializers.SerializerMethodField()
    percentage = serializers.SerializerMethodField()
    difference = serializers.SerializerMethodField()

    class Meta:
        model = CarAnnouncement
        fields = (
            'id',
            'model',
            'price',
            'average_price',
            'percentage',
            'difference'
        )

    def get_average_price(self, obj):
        return CarAnnouncement.objects.filter(model=obj.model).aggregate(
            average_price=Avg('price')
        )['average_price']

    def get_percentage(self, obj):
        return obj.price / self.get_average_price(obj) * 100

    def get_difference(self, obj):
        average = self.get_average_price(obj)
        difference = obj.price - average
        if difference < 0:
            is_good = True
            difference *= -1
        else:
            is_good = False
        percentage = difference / average * 100
        return {
            'amount': difference,
            'is_good': is_good,
            'percentage': percentage
        }