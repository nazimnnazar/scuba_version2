# Generated by Django 4.1 on 2023-06-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantform', '0032_team_hotelname'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=100)),
            ],
        ),
    ]
