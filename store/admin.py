from django.contrib import admin
from .models import *
from django.conf import settings
# from . import models

admin.site.register(CustomUser)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'description', 'price']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']


@admin.register(PurchaseOrderItem)
class PurchaseOrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'purchase_order']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'unit_price', 'quantity', 'sale_order']
