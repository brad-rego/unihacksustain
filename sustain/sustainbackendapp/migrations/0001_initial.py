# Generated by Django 2.1 on 2018-08-04 13:39

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.IntegerField()),
                ('username', models.CharField(max_length=40)),
                ('comment', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60)),
                ('rating', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('imgUrl', models.CharField(default=None, max_length=120)),
                ('address', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=60)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('restaurant', models.IntegerField()),
                ('score', models.IntegerField()),
                ('waterUp', models.IntegerField(default=0)),
                ('waterDown', models.IntegerField(default=0)),
                ('wasteUp', models.IntegerField(default=0)),
                ('wasteDown', models.IntegerField(default=0)),
                ('localUp', models.IntegerField(default=0)),
                ('localDown', models.IntegerField(default=0)),
                ('vegetarianUp', models.IntegerField(default=0)),
                ('vegetarianDown', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
