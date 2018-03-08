# Generated by Django 2.0 on 2018-02-05 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actor', '0017_auto_20180205_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Comment')),
                ('pub_date', models.DateTimeField(default='', verbose_name='Date of comment')),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actor.Actor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.TextField(default=''),
        ),
    ]