# Generated by Django 4.2.3 on 2023-07-04 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_cuenta_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
