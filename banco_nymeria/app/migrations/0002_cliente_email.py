# Generated by Django 2.1.7 on 2019-02-16 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='contato@contato.com', max_length=255, verbose_name='E-mail'),
        ),
    ]
