# Generated by Django 2.2.7 on 2019-11-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191117_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/img/default.jpg', upload_to='profile_pics'),
        ),
    ]
