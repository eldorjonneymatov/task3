from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from apps.car_announcements.models import CarAnnouncement
from .serializers import CarAnnouncementSerializer

class AnnouncementDetailView(RetrieveAPIView):
    model_class = CarAnnouncement
    serializer_class = CarAnnouncementSerializer
    queryset = CarAnnouncement.objects.all()