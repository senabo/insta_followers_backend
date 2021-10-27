from django.urls import path

from app.pkg.account.api.views import SocialAuthView


urlpatterns = [
    path('auth/signup/social/', SocialAuthView.as_view(), name='signup-social'),
]
