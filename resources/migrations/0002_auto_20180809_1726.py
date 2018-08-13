# Generated by Django 2.0.5 on 2018-08-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UseControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateTimeField(auto_now_add=True)),
                ('date_ended', models.DateTimeField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete='', to='resources.Driver')),
                ('vehicle', models.ForeignKey(on_delete='', to='resources.Vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='usecontrols',
            field=models.ManyToManyField(through='resources.UseControl', to='resources.Driver'),
        ),
    ]