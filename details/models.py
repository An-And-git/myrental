from django.db import models

# Create your models here.

FURNISH = (('Fully furnished', 'FULLY FURNISHED'),
            ('Semi furnished', 'SEMI FURNISHED'),
            ('Unfurnished', 'UNFURNISHED'))

class Details(models.Model):
    #Shop Details
    shop_name = models.CharField(max_length=255)
    tenant_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    furnished = models.CharField(max_length=100, choices=FURNISH, default='Unfurnished')
    size = models.CharField(max_length=255)
    #contact details
    tenant_phone = models.CharField(max_length=255)
    tenant_address = models.TextField()

    def __str__(self):
        return self.shop_name