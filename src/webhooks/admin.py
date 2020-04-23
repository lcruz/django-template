from django.contrib import admin
from .models import WebHook


class WebHookAdmin(admin.ModelAdmin):
    list_display = ('event', 'endpoint', 'created_at', 'last_attempt_code', 'last_attempt_date')

    def event(self, obj):
        return "%s.%s" % (obj.event_object, obj.event_action)

admin.site.register(WebHook, WebHookAdmin)