# Generated by Django 4.1 on 2023-04-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantform', '0021_rename_admi_checkin_team_admin_checkin'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='island',
            field=models.CharField(choices=[('Kavaratti', 'Kavaratti'), ('Agatti', 'Agatti'), ('Kadmat', 'Kadmat'), ('Minicoy', 'Minicoy'), ('Kalpeni', 'Kalpeni')], default=1, max_length=240),
            preserve_default=False,
        ),
    ]
