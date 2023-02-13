from django.db import models
from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField
from django.conf import settings


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    billing_street = models.CharField(max_length=255)
    billing_city = models.CharField(max_length=255)
    billing_postal_code = models.PositiveIntegerField(null=True)
    shipping_street = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=255)
    shipping_postal_code = models.IntegerField(null=True)
    phone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    description = models.TextField()
    # insert image field
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='PHP')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # product = models.ForeignKey(
    #     Product, related_name='images', on_delete=models.CASCADE)


class PurchaseOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"purchase order by {self.user.username}"


class PurchaseOrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class Sale(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"purchased by {self.user.username}"


class SaleItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE
    )
    unit_price = MoneyField(
        max_digits=14, decimal_places=2, default_currency='PHP')

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
