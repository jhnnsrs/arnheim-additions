# Generated by Django 2.2.9 on 2020-03-02 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elements', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transformer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('channel', models.CharField(default='Not active', max_length=100, unique=True)),
                ('settings', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transforming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statuscode', models.IntegerField(blank=True, null=True)),
                ('statusmessage', models.CharField(blank=True, max_length=500, null=True)),
                ('settings', models.CharField(max_length=1000)),
                ('nodeid', models.CharField(blank=True, max_length=400, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('experiment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elements.Experiment')),
                ('representation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elements.Representation')),
                ('roi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elements.ROI')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elements.Sample')),
                ('transformer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transformers.Transformer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
