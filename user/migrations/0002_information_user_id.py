# Generated by Django 3.0 on 2019-12-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='user_id',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
