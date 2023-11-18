# Generated by Django 4.2.7 on 2023-11-18 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('A1', 'A2'), ('B1', 'B2')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(upload_to='course_covers/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('program', models.TextField()),
                ('what_you_learn', models.TextField()),
                ('bonus', models.TextField()),
                ('modules', models.PositiveIntegerField()),
                ('lessons', models.PositiveIntegerField()),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.difficulty')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.language')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.price')),
            ],
        ),
    ]