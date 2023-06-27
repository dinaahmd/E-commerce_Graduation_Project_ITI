from django.contrib import admin
from .models import ProductCategory, ProductItem, Promotion
from django.db import models


admin.site.register(ProductCategory)
admin.site.register(Promotion)

class ProductAdmin(admin.ModelAdmin):
    # make the discount_price field optional in the admin dashboard
    formfield_overrides = {
        models.FloatField: {'required': False},
    }

admin.site.register(ProductItem, ProductAdmin)