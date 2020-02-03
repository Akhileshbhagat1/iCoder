# Generated by Django 2.2.2 on 2020-01-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]