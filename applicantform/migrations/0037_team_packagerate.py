# Generated by Django 4.1 on 2023-07-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantform', '0036_alter_team_room_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='packagerate',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=1000000, null=True),
        ),
    ]