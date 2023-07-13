# Generated by Django 4.1 on 2023-07-11 06:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_invoice_prepayment_alter_invoice_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='num_guests',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='num_rooms',
        ),
        migrations.AddField(
            model_name='invoice',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='package',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]