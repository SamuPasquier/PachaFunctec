# Generated by Django 4.2.4 on 2024-10-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pachamodel', '0003_usuario_brillo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='multipacha',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
