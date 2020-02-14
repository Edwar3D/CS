# Generated by Django 3.0.3 on 2020-02-13 15:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20200213_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCiudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Ciudad',
            },
        ),
        migrations.CreateModel(
            name='ModelEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='ModelEstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoCivil', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'EstadoCivil',
            },
        ),
        migrations.CreateModel(
            name='ModelGenero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=50)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Genero',
            },
        ),
        migrations.CreateModel(
            name='ModelOcupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Ocupacion',
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelCiudad'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelEstado'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estadoCivil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelEstadoCivil'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelGenero'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ocupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelOcupacion'),
        ),
    ]