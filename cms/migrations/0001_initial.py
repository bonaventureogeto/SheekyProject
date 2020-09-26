# Generated by Django 3.1.1 on 2020-09-25 12:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggested_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('email_verified_at', models.DateField(null=True)),
                ('phone_no', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=255)),
                ('residence', models.CharField(max_length=50)),
                ('age_group', models.CharField(max_length=10)),
                ('favorite_hairstyle', models.CharField(max_length=50)),
                ('like_about_your_hair', models.TextField(blank=True)),
                ('daily_hair_ritual', models.TextField(blank=True)),
                ('products_used', models.CharField(max_length=255)),
                ('skin_problem', models.CharField(max_length=255)),
                ('profile_pic', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('join_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('email_verification_code', models.CharField(max_length=50, null=True)),
                ('sheekyhub_post', models.TextField(blank=True)),
                ('my_reviews', models.TextField(blank=True)),
                ('previous_treatment_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('previous_treatment_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('previous_treatment_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('previous_treatment_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.TextField(blank=True)),
                ('solution', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('about_us', models.TextField()),
                ('facebook_link', models.CharField(max_length=255)),
                ('twitter_link', models.CharField(max_length=255)),
                ('youtube_link', models.CharField(max_length=255)),
                ('snapchat_link', models.CharField(max_length=255)),
                ('linkedin_link', models.CharField(max_length=255)),
                ('instagram_link', models.CharField(max_length=255)),
                ('latest_youtube_video_link', models.CharField(max_length=255)),
                ('background_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('testimonials', models.TextField(blank=True)),
                ('testimonial_author', models.CharField(default='anonymous', max_length=255)),
                ('testimonial_author_position', models.CharField(default='unknown', max_length=255)),
                ('testimonial_author_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.department')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.department')),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('staff_assigned', models.CharField(max_length=100)),
                ('main_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_9', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.department')),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.servicecategory')),
                ('service_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.servicesubcategory')),
            ],
        ),
    ]
