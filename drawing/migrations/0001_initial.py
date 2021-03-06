# Generated by Django 2.2.9 on 2020-03-02 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineROI',
            fields=[
                ('roi_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='elements.ROI')),
                ('length', models.IntegerField()),
            ],
            bases=('elements.roi',),
        ),
    ]
