# Generated by Django 4.2.3 on 2023-07-04 05:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_alter_pedidos_direccion_alter_pedidos_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='direccion',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5, message='direccion invalida, debe ingresar una direccion correcta.')]),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(4, message='El nombre es demasiado corto.')]),
        ),
    ]
