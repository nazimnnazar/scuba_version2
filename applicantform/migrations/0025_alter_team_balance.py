# Generated by Django 4.1 on 2023-04-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantform', '0024_team_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=1000000),
        ),
    ]
