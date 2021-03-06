# Generated by Django 3.0.6 on 2020-07-19 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Candidat', '0004_auto_20200711_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='type_diplome',
            field=models.CharField(choices=[('', '(Degree)'), ('CPGE/BTS/DEUG/...', 'CPGE/BTS/DEUG/...'), ('Licence', 'Licence '), ('Master', 'Master'), ('Doctorat', 'Doctorat')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.CharField(choices=[('', '(Level)'), ('A1', 'découverte'), ('A2', 'usuel'), ('B1', 'niveau seuil'), ('B2', 'niveau avancé'), ('C1', 'autonome'), ('C2', 'maîtrise')], max_length=2, null=True),
        ),
        migrations.CreateModel(
            name='Personalite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openness', models.IntegerField()),
                ('conscientiousness', models.IntegerField()),
                ('extraversion', models.IntegerField()),
                ('agreeableness', models.IntegerField()),
                ('neuroticism', models.IntegerField()),
                ('profil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Candidat.Profil')),
            ],
        ),
    ]
