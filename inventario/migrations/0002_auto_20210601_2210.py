# Generated by Django 3.1.7 on 2021-06-02 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipotransporte',
            name='estado',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='tipotransporte',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]