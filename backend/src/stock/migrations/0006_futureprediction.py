# Generated by Django 2.1.5 on 2019-11-05 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_historyprediction'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuturePrediction',
            fields=[
                ('symbol', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('insample', models.TextField()),
                ('outsample', models.TextField()),
                ('result', models.TextField()),
                ('insampleMse', models.FloatField()),
                ('insampleR2', models.FloatField()),
            ],
            options={
                'db_table': 'futurePrediction',
            },
        ),
    ]
