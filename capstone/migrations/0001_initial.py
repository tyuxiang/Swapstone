# Generated by Django 3.0.3 on 2020-03-23 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=20)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10, max_length=5)),
                ('width', models.DecimalField(decimal_places=2, max_digits=10, max_length=5)),
                ('area', models.DecimalField(decimal_places=2, max_digits=10, max_length=5)),
                ('project_name', models.CharField(max_length=100)),
                ('position_x', models.DecimalField(decimal_places=2, max_digits=10, max_length=100)),
                ('position_y', models.DecimalField(decimal_places=2, max_digits=10, max_length=100)),
                ('in_campus_centre', models.BooleanField()),
            ],
        ),
    ]
