# Generated by Django 3.2.12 on 2023-07-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='exam_name',
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
