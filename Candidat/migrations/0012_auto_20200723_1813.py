# Generated by Django 3.0.6 on 2020-07-23 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Candidat', '0011_auto_20200723_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='sex',
            field=models.CharField(choices=[('', '(Gender)'), ('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='user',
            field=models.OneToOneField(default='images/user.png', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
