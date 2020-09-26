from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField('Date created')
    updated_at = models.DateTimeField('Date updated')

    def __str__(self):
        return self.category_name