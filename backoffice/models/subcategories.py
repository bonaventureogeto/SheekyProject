from django.db import models

class Subcategory(models.Model):
    sub_category_name = models.CharField(max_length=255)
    category_id = models.IntegerField()
    created_at = models.DateTimeField('Date created')
    updated_at = models.DateTimeField('Date updated')

    def __str__(self):
        return self.sub_category_name