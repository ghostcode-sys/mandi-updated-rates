# Generated by Django 3.0.8 on 2020-10-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=100)),
                ('psw', models.CharField(max_length=75)),
                ('location', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_name', models.CharField(max_length=50)),
                ('price', models.BigIntegerField(default=0.0)),
                ('location', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=75)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=100)),
                ('psw', models.CharField(max_length=75)),
                ('location', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=75)),
            ],
        ),
    ]