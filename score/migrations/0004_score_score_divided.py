# Generated by Django 4.1.5 on 2023-02-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0003_score_score_multiple'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='score_divided',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]