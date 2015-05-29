# -*-coding=utf-8-*-
from django.db import models
from django.utils.timezone import now

class Product(models.Model):
    name           = models.CharField(max_length=100)
    brand_type     = models.TextField()
    description    = models.TextField(null=True, blank=True)
    create_time    = models.DateTimeField(default=now)
    update_time    = models.DateTimeField(auto_now=True)

    def get_price_list(self):
        return Price.objects.filter(product=self)

    def __unicode__(self):
        return u"%d-%s" % (self.id if self.id  is not None else 0, self.name)


class Price(models.Model):
    HIGH = 'high'
    STANDARD = 'standard'
    LOW = 'low'

    CONFIG_CHOICES = (
        (HIGH, u'高配'),
        (STANDARD, u'标配'),
        (LOW, u'低配')  
    )

    product = models.ForeignKey(Product)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    config_type = models.CharField(max_length=10, choices=CONFIG_CHOICES, default=STANDARD)
    create_time    = models.DateTimeField(default=now)
    update_time    = models.DateTimeField(auto_now=True)

        


# class  LineItem(models.Model):
#     prduct = models.ForeignKey(Product)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.IntegerField()


# class Cart(object):  
#     def __init__(self, *args, **kwargs):  
#         self.items = []  
#         self.total_price = 0  
#     def add_product(self, product):  
#         self.total_price += product.price  
#         for item in self.items:  
#             if item.product.id == product.id:  
#                 item.quantity += 1   
#                 return  
#         self.items.append(LineItem(product=product,unit_price=product.price,quantity=1))
