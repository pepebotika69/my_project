# Generated by Django 4.0.3 on 2022-03-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='name',
        ),
        migrations.AddField(
            model_name='animal',
            name='name_female',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Animal female name'),
        ),
        migrations.AddField(
            model_name='animal',
            name='name_male',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Animal male name'),
        ),
    ]
