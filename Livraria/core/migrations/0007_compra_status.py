# Generated by Django 5.0.1 on 2024-01-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='status',
            field=models.IntegerField(choices=[(1, 'Carrinho'), (2, 'Realizado'), (3, 'Pago'), (4, 'Entregue')], default=1),
        ),
    ]
