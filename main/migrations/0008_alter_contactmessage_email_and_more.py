# Generated by Django 4.2.7 on 2023-12-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(max_length=500, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='reason',
            field=models.CharField(max_length=100, verbose_name='Reason'),
        ),
    ]
