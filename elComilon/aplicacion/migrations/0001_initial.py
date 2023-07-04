# Generated by Django 4.2.3 on 2023-07-04 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('rut', models.CharField(error_messages='Debe ingresar rut', max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('saldo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_prod', models.IntegerField(error_messages='Debe ingresar el id del producto', primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.IntegerField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=50)),
                ('nombre', models.ForeignKey(db_column='nombre', on_delete=django.db.models.deletion.CASCADE, to='aplicacion.cuenta')),
            ],
        ),
    ]