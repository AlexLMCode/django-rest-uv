# Generated by Django 3.2.3 on 2021-06-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idmunicipio', models.IntegerField()),
                ('identidad', models.IntegerField()),
                ('nombre_municipio', models.CharField(max_length=200)),
            ],
        ),
    ]
