# Generated by Django 4.2.4 on 2023-08-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStoreModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
