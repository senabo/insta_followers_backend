from django.contrib import admin

from app.pkg.hello.models import HelloMessage


@admin.register(HelloMessage)
class HelloAdmin(admin.ModelAdmin):
    list_display = ('message',)
