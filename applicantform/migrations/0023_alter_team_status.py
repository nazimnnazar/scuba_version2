# Generated by Django 4.1 on 2023-04-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantform', '0022_team_island'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('open', 'open'), ('Confirm', 'Confirm'), ('Closed', 'Closed'), ('Completed', 'Completed')], default='Processing', max_length=100),
        ),
    ]