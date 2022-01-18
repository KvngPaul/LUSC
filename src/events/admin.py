from django.contrib import admin

from .models import (
    Session,
    TransportEvent,
    LuggageEvent,
    TradeFairEvent,
)

admin.site.register(Session)
admin.site.register(TransportEvent)
admin.site.register(LuggageEvent)
admin.site.register(TradeFairEvent)