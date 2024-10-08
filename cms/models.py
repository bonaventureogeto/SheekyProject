from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Customer(models.Model):
    """ 
    model for customer 
    """
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    email_verified_at = models.DateField(null=True)
    phone_no = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    residence = models.CharField(max_length=50)
    age_group = models.CharField(max_length=10)
    favorite_hairstyle = models.CharField(max_length=50)
    like_about_your_hair = models.TextField(blank=True)
    daily_hair_ritual = models.TextField(blank=True)
    products_used = models.CharField(max_length=255)
    skin_problem = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    join_date = models.DateTimeField(default=datetime.now, blank=True)
    email_verification_code = models.CharField(max_length=50, null=True)
    sheekyhub_post = models.TextField(blank=True)
    my_reviews = models.TextField(blank=True)
    previous_treatment_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    previous_treatment_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    previous_treatment_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    previous_treatment_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    models for departments in sheeky
    """
    department_name = models.CharField(max_length=100)

    def __str__(self):
        """repr for department"""
        return self.department_name


class ServiceCategory(models.Model):
    """ 
    models for service category
    """
    category_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        """repr for service category"""
        return self.category_name


class ServiceSubCategory(models.Model):
    """ 
    models for service subcategory
    """
    subcategory_name = models.CharField(max_length=100)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        """repr for service subcategory"""
        return self.subcategory_name


class Service(models.Model):
    """ 
    models for services offered in Barber and Salon 
    """
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    description = models.TextField()
    staff_assigned = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_subcategory = models.ForeignKey(ServiceSubCategory, on_delete=models.CASCADE)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        """repr for service"""
        return self.name


class Product(models.Model):
    """
    model for product
    """
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        """ repr for product """
        return self.product_name


class Booking(models.Model):
    """
    models for booking
    """
    appointment_date = models.CharField(max_length=255)
    appointment_time = models.CharField(max_length=100)
    user_id = models.IntegerField()

    def __str__(self):
        """repr for booking"""
        return self.appointment_time


class IndexPage(models.Model):
    """
    models for index page
    """
    email = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    about_us = models.TextField()
    facebook_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255)
    snapchat_link = models.CharField(max_length=255)
    linkedin_link = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255)
    latest_youtube_video_link = models.CharField(max_length=255)
    background_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    testimonials = models.TextField(blank=True)
    testimonial_author = models.CharField(max_length=255, default='anonymous')
    testimonial_author_position = models.CharField(max_length=255, default='unknown')
    testimonial_author_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    
    def __str__(self):
        """repr for contact us"""
        return self.email


class Help(models.Model):
    """
    models for FAQs
    """
    problem = models.TextField(blank=True)
    solution = models.TextField(blank=True)

    def __str__(self):
        """repr for help"""
        return self.problem
