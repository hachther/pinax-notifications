# Generated by Django 4.1.3 on 2022-11-04 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_notifications', '0002_auto_20171003_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticequeuebatch',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='noticesetting',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='noticesetting',
            name='medium',
            field=models.CharField(choices=[(0, 'email'), (1, 'push'), (2, 'in_app'), (3, 'telegram')], max_length=1, verbose_name='medium'),
        ),
        migrations.AlterField(
            model_name='noticetype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]