from rest_framework import viewsets

from app.pkg.hello.api.serialilzers import HelloSerializer
from app.pkg.hello.models import HelloMessage


class HelloView(viewsets.ModelViewSet):
    serializer_class = HelloSerializer
    queryset = HelloMessage.objects.all()
