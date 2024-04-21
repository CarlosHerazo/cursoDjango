# Generated by Django 5.0.4 on 2024-04-14 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionPedidos', '0002_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='direccion_cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email_cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='nombre_cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tlf',
            field=models.CharField(max_length=50, verbose_name='telefono_cliente'),
        ),
    ]