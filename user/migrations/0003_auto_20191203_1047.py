# Generated by Django 3.0 on 2019-12-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_information_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
