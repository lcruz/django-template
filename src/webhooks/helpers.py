import requests
from .models import WebHook
from django.utils import timezone
from rest_framework import status
import json


def call_webhooks(event_object, event_action, data):
    web_hooks = WebHook.objects.filter(event_object=event_object, event_action=event_action)
    for web_hook in web_hooks:
        call_webhook(web_hook, data)


def call_webhook(web_hook, data):
    params = {
        "event_object": web_hook.event_object,
        "event_action": web_hook.event_action,
        "data": data
    }

    if not web_hook.envelope:
        params = data

    try:
        headers = None
        if web_hook.authorization:
            headers = {'Authorization': web_hook.authorization}
        web_hook.last_attempt_date = timezone.now()
        r = requests.post(web_hook.endpoint, json=params, headers=headers)

        web_hook.last_input = json.dumps(params)
        web_hook.last_attempt_code = r.status_code
        web_hook.last_content = r.content.decode('utf-8')
        web_hook.save()

        if r.status_code == status.HTTP_200_OK:
            return

    except requests.ConnectionError:
        web_hook.last_attempt_code = 500
        web_hook.save()


