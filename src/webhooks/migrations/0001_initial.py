# Generated by Django 2.1.2 on 2018-12-21 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebHook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(max_length=255)),
                ('event_object', models.CharField(choices=[('team', 'Equipo')], max_length=20)),
                ('event_action', models.CharField(choices=[('added', 'Agregado'), ('updated', 'Actualizado'), ('deleted', 'Borrado')], max_length=20)),
                ('http_user', models.CharField(blank=True, max_length=50, null=True)),
                ('http_pass', models.CharField(blank=True, max_length=50, null=True)),
                ('last_attempt_code', models.IntegerField(blank=True, null=True)),
                ('last_attempt_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
