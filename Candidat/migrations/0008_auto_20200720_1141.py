# Generated by Django 3.0.6 on 2020-07-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidat', '0007_auto_20200720_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='agreeableness',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='conscientiousness',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='extraversion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='neuroticism',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='openness',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
