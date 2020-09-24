from django.db import models
from datetime import datetime


class Customer(models.Model):
    """ model for customer """
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
    profile_pic = models.CharField(max_length=50)
    join_date = models.DateTimeField(default=datetime.now, blank=True)
    email_verification_code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

