from django.db import models

# Create your models here.

SHOP_CHOICES = (
    ('Vasantham Hardwares','VASANTHAM HARDWARES'),
    ('Vijay Plywoods', 'VIJAY PLYWOODS'),
    ('Shanti Plywoods','SHANTI PLYWOODS'),
    ('Vasantham Office','VASANTHAM OFFICE'),
)
STATUS_OPTIONS = (('Received', 'RECEIVED'),
                    ('Pending', 'PENDING'))

class Dashboard(models.Model):
    shop = models.CharField(max_length=100, choices=SHOP_CHOICES, default='Vasantham Hardwares')
    tenant_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rental_month = models.DateField()
    due_date = models.DateField()
    give_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_OPTIONS, default='Pending')
    note = models.TextField()

    def __str__(self):
        return self.shop

    def notes(self):
        return self.note[:100]

    def rental_month_pretty(self):
        return self.rental_month.strftime('%B')

    def due_date_pretty(self):
        return self.due_date('%b %e %Y')