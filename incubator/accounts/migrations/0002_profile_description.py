# Generated by Django 2.2.7 on 2019-11-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
