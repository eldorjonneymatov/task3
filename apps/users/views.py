from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    model_class = User
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
