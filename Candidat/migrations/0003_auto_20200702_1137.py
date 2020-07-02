# Generated by Django 3.0.6 on 2020-07-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidat', '0002_profil_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='type_diplome',
            field=models.CharField(choices=[('CPGE/BTS/DEUG/...', 'CPGE/BTS/DEUG/...'), ('Licence', 'Licence '), ('Master', 'Master'), ('Doctorat', 'Doctorat')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='sex',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='status',
            field=models.CharField(choices=[('célibataire', 'célibataire'), ('marié(e)', 'marié(e)'), ('veuf(ve)', 'veuf(ve)'), ('divorcé(e)', 'divorcé(e)')], max_length=12, null=True),
        ),
    ]
