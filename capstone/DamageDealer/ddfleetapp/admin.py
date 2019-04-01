from django.contrib import admin

from .models import Card, Fleet, CardAmount

admin.site.register(Card)
admin.site.register(Fleet)
admin.site.register(CardAmount)
