from rest_framework import serializers

from app.pkg.hello.models import HelloMessage


class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloMessage
        fields = '__all__'
