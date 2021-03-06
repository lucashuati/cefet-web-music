# Generated by Django 2.1.3 on 2018-11-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musico',
            name='genero',
            field=models.CharField(default='Masculino', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='musico',
            name='bandas',
            field=models.ManyToManyField(related_name='musicos', to='music.Banda'),
        ),
    ]
