# Generated by Django 4.0.3 on 2022-08-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
                ('comments', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='images/news/')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='PricingFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
                ('position', models.CharField(default='Innovation Officer', max_length=100)),
                ('image', models.ImageField(upload_to='images/team/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
                ('position', models.CharField(default='CEO, First Choice Group', max_length=100)),
                ('image', models.ImageField(upload_to='images/clients/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='project',
            name='about',
            field=models.TextField(default='Nats Stenman began his career in construction with boots on the ground'),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
                ('image1', models.ImageField(upload_to='images/services/')),
                ('image2', models.ImageField(upload_to='images/services/')),
                ('icon', models.ImageField(upload_to='images/services/')),
                ('solutions', models.ManyToManyField(to='home.solution')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('features', models.ManyToManyField(to='home.pricingfeatures')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
