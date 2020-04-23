from django.db import models


class WebHook(models.Model):

    EVENT_OBJECT_BUSINESS = 'business'
    EVENT_ACTION_CREATED = 'created'
    EVENT_ACTION_UPDATED = 'updated'
    EVENT_ACTION_DELETED = 'deleted'

    EVENT_OBJECT_CHOICES = (
        (EVENT_OBJECT_BUSINESS, 'Negocio'),
    )

    EVENT_ACTION_CHOICES = (
        ('created', 'Creación'),
        ('updated', 'Actualización'),
        ('deleted', 'zEliminación')
    )

    endpoint = models.CharField(max_length=255, verbose_name='End Point')
    event_object = models.CharField(max_length=20, choices=EVENT_OBJECT_CHOICES, verbose_name="Objeto")
    event_action = models.CharField(max_length=20, choices=EVENT_ACTION_CHOICES, verbose_name="Acción")
    http_user = models.CharField(max_length=50, null=True, blank=True, verbose_name="Usuario HTTP")
    http_pass = models.CharField(max_length=50, null=True, blank=True, verbose_name="Contraseña HTTP")
    authorization = models.CharField(max_length=255, null=True, blank=True)
    last_attempt_code = models.IntegerField(null=True, blank=True, verbose_name="Código de respuesta del último itento")
    last_attempt_date = models.DateTimeField(null=True, blank=True, verbose_name="Úlitma fecha de intento")
    last_input = models.TextField(null=True, blank=True)
    envelope = models.BooleanField(null=True, blank=True, default=True)
    last_content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización")

    def __str__(self):
        return "%s.%s" % (self.event_object, self.event_action)
