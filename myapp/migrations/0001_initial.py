# Generated by Django 4.2.5 on 2023-09-16 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filiereNom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stagiaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('stgMatricule', models.CharField(max_length=4)),
                ('mobile', models.CharField(max_length=10)),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.filiere')),
            ],
        ),
    ]
