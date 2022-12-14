# Generated by Django 4.1 on 2022-08-18 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название тэга')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('-upload_date',), 'verbose_name': 'Видеозапись', 'verbose_name_plural': 'Видеозаписи'},
        ),
        migrations.AddField(
            model_name='video',
            name='categories',
            field=models.ManyToManyField(related_name='videos', to='videos.category', verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(related_name='videos', to='videos.tag', verbose_name='Тэги'),
        ),
    ]
