# Generated by Django 3.1.1 on 2020-09-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateTimeField()),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('weight', models.PositiveIntegerField()),
                ('growth', models.PositiveIntegerField()),
            ],
        ),
    ]
