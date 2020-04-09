# Generated by Django 3.0.3 on 2020-04-09 08:45

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
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('curr_map_ref', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=20)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10, max_length=5)),
                ('width', models.DecimalField(decimal_places=2, max_digits=10, max_length=5)),
                ('area', models.DecimalField(decimal_places=2, max_digits=10, max_length=5)),
                ('project_name', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('length_pixel', models.DecimalField(decimal_places=2, max_digits=10, max_length=5)),
                ('width_pixel', models.DecimalField(decimal_places=2, max_digits=10, max_length=5)),
                ('rotation', models.DecimalField(decimal_places=2, default=-1, max_digits=10, max_length=5)),
                ('position_x', models.DecimalField(decimal_places=2, default=-1, max_digits=10, max_length=100)),
                ('position_y', models.DecimalField(decimal_places=2, default=-1, max_digits=10, max_length=100)),
                ('in_campus_centre', models.BooleanField()),
                ('saved_map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booths', to='capstone.Map')),
            ],
        ),
    ]
