# Generated by Django 2.2 on 2019-09-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0006_webhook_last_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='envelope',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
