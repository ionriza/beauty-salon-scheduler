# Generated by Django 5.0.3 on 2024-03-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='photo',
            field=models.ImageField(default='', upload_to='salons/'),
            preserve_default=False,
        ),
    ]