# Generated by Django 2.0 on 2018-01-29 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0004_auto_20180129_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prizeName', models.CharField(max_length=500)),
                ('PrizeDate', models.CharField(max_length=250)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actor.Actor')),
            ],
        ),
    ]