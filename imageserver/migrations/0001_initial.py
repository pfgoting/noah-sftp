# Generated by Django 3.1.7 on 2021-03-06 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hour_accum', models.IntegerField()),
                ('file', models.ImageField(upload_to='images')),
            ],
        ),
    ]
