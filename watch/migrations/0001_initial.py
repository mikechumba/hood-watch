# Generated by Django 2.1.7 on 2019-03-21 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tel', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('amenity_type', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Businesses',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Post'),
        ),
        migrations.AddField(
            model_name='business',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Profile'),
        ),
        migrations.AddField(
            model_name='amenities',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Neighbourhood'),
        ),
    ]