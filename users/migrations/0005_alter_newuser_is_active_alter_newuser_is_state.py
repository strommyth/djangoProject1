# Generated by Django 4.0.2 on 2022-02-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_newuser_is_state_alter_newuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='啟用'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_state',
            field=models.CharField(choices=[('SEC404', '階段一'), ('SEC303', '階段二'), ('SEC202', '階段三')], default='SEC404', max_length=150),
        ),
    ]
