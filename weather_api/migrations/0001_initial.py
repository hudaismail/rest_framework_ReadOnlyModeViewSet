# Generated by Django 3.1.7 on 2021-03-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_description', models.IntegerField(choices=[(0, 'Sunny'), (0, 'Sunny'), (0, 'Sunny'), (0, 'Sunny')], default=0)),
                ('temperature', models.FloatField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
