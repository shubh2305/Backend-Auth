# Generated by Django 3.2.5 on 2021-11-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211116_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='decription',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_finished',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
