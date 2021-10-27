import requests
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from rest_framework.reverse import reverse
from social_core.exceptions import MissingBackend
from social_django.utils import load_strategy, load_backend
from social_django.views import NAMESPACE

User = get_user_model()


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ('auth_token',)


class SocialAuthSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    provider = serializers.CharField()

    default_error_messages = {
        'invalid_provider': _('Invalid auth provider'),
    }

    def init(self, *args, **kwargs):
        self.user = None
        super(SocialAuthSerializer, self).init(*args, **kwargs)

    def validate(self, attrs):
        provider = attrs.get('provider')
        access_token = attrs.get('access_token')
        strategy = load_strategy(request=self.context['request'])

        try:
            backend = load_backend(strategy, provider, reverse(NAMESPACE + ":complete", args=(provider,)))
        except MissingBackend:
            self.fail('invalid_provider')

        try:
            self.user = backend.do_auth(access_token=access_token)
        except requests.HTTPError as e:
            raise serializers.ValidationError(e.response.text)

        return super(SocialAuthSerializer, self).validate(attrs)

    def create(self, validated_data):
        return self.user

    def to_representation(self, instance):
        token, _ = Token.objects.get_or_create(user=self.user)
        return TokenSerializer(instance=token, context=self.context).data
