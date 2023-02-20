# Generated by Django 4.1.7 on 2023-02-20 18:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Videogame',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapi.company')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapi.genre')),
            ],
        ),
        migrations.CreateModel(
            name='VideogameImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('videogame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapi.videogame')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('jwt', models.CharField(max_length=500)),
                ('sign_in', models.CharField(max_length=120)),
                ('sign_out', models.CharField(max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapi.user')),
                ('videogame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapi.videogame')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapi.user')),
                ('videogame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameapi.videogame')),
            ],
        ),
    ]
