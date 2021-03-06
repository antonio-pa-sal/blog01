# Generated by Django 2.2.15 on 2020-08-18 17:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200818_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.CharField(choices=[('normal', 'Normal'), ('featured', 'Featured')], default='normal', max_length=15, verbose_name='Destacado'),
        ),
        migrations.AddField(
            model_name='post',
            name='promoted',
            field=models.CharField(choices=[('normal', 'Normal'), ('promoted', 'Promoted')], default='normal', max_length=15, verbose_name='Promocionado'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body2',
            field=ckeditor.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='body3',
            field=ckeditor.fields.RichTextField(blank=True, default=''),
        ),
    ]
