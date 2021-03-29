from django.contrib import admin
from .models import Product, Category, RatingProducts


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class RatingProductsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'rate',
        'rate_comment',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RatingProducts, RatingProductsAdmin)
