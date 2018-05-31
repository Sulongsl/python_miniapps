# Generated by Django 2.0.4 on 2018-05-28 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=44)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_1', models.ManyToManyField(to='polls.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=66)),
                ('text', models.TextField()),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='FileClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('file_date', models.FileField(upload_to='uploads/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='FilePathClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FilePathField(match='foo.*', path='/home/images', recursive=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='None', upload_to='images/', width_field='None')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MySpecialSser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='supervisor_of', to=settings.AUTH_USER_MODEL)),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=40)),
                ('person_age', models.IntegerField()),
                ('create_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='channel_2',
            field=models.ManyToManyField(to='polls.Manufacturer'),
        ),
        migrations.AddField(
            model_name='car',
            name='maunfacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Manufacturer'),
        ),
    ]
