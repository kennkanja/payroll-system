# Generated by Django 3.2.12 on 2023-07-18 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0004_home'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecturer',
            old_name='quality',
            new_name='quantity',
        ),
    ]
