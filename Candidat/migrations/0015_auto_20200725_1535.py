# Generated by Django 3.0.6 on 2020-07-25 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Entreprise', '0003_auto_20200723_1806'),
        ('Candidat', '0014_auto_20200724_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience_pro',
            name='nbr_annnee',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='poste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Entreprise.Poste'),
        ),
    ]