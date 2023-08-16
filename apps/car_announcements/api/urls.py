from django.urls import path
from .views import AnnouncementDetailView


urlpatterns = [
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail')
]