from django.db import models

class Customer(models.Model):
    """ model for customer """
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_langth=20)
    email = models.EmailField(unique=True)
    email_verified_at = models.DateField(null=True)
    phone_no = models.CharField(max_langth=15)
    password = models.PasswordField(max_langth=255)
    residence = models.CharField(max_langth=50)
    age_group = model.CharField(max_langth=10)
    favorite_hairstyle = models.CharField(max_langth=50)
    like_about_your_hair = models.CharField(max_length=255)
    daily_hair_ritual = models.CharField(max_langth=255)
    products_used = models.CharField(max_langth=255)
    skin_problem = models.CharField(max_langth=255)
    profile_pic = models.CharField(max_langth=50)
    join_date = models.DateField(default=timezone.now)
    email_verification_code = models.CharField(max_langth=50, null=True)

     def __str__(self):
        return self.name

