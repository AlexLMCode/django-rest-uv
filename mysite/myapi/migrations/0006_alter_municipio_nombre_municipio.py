# Generated by Django 3.2.3 on 2021-06-04 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='nombre_municipio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]