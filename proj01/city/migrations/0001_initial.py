# Generated by Django 2.1.5 on 2019-01-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('population', models.IntegerField(default=0)),
                ('date_mod', models.DateField()),
            ],
        ),
    ]
