# Generated by Django 5.0.3 on 2024-04-18 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evento_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
