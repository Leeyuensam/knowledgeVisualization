# Generated by Django 3.0.6 on 2020-07-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, verbose_name='发表时间')),
                ('title', models.TextField(max_length=5000, verbose_name='标题')),
                ('content', models.TextField(max_length=5000, verbose_name='内容')),
                ('source_url', models.TextField(max_length=5000, verbose_name='来源url')),
                ('ents', models.TextField(blank=True, max_length=5000, null=True, verbose_name='实体')),
            ],
            options={
                'verbose_name': '新闻信息',
                'verbose_name_plural': '新闻信息',
            },
        ),
        migrations.CreateModel(
            name='research_papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, verbose_name='发表时间')),
                ('authors', models.TextField(max_length=5000, verbose_name='作者')),
                ('title', models.TextField(max_length=5000, verbose_name='标题')),
                ('abstract', models.TextField(max_length=5000, verbose_name='摘要')),
                ('ents', models.TextField(blank=True, max_length=5000, null=True, verbose_name='实体')),
            ],
            options={
                'verbose_name': '科研论文信息',
                'verbose_name_plural': '科研论文信息',
            },
        ),
        migrations.CreateModel(
            name='rumors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.CharField(max_length=100, verbose_name='发表时间')),
                ('rumor', models.TextField(max_length=5000, verbose_name='标题')),
                ('fact', models.TextField(max_length=5000, verbose_name='内容')),
                ('ents', models.TextField(blank=True, max_length=5000, null=True, verbose_name='实体')),
            ],
            options={
                'verbose_name': '谣言信息',
                'verbose_name_plural': '谣言信息',
            },
        ),
    ]
