# Generated by Django 3.2.3 on 2021-06-04 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_actividad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
    ]
