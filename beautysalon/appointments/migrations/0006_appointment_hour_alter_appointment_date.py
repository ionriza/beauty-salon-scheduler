# Generated by Django 5.0.3 on 2024-03-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_appointment_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='hour',
            field=models.TimeField(default='00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
    ]
