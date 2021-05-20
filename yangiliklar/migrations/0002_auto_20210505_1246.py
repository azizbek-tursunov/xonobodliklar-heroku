# Generated by Django 2.1.5 on 2021-05-05 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yangiliklar', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yangilik',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='yangilik',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media', verbose_name='Rasm'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='yangilik',
            name='qisqa',
            field=models.TextField(),
        ),
    ]