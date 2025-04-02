from django.contrib import admin
from django.utils.html import format_html
from .models import CoffeeType, Order

class CoffeeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'display_image')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    
    display_image.allow_tags = True
    display_image.short_description = "Preview"

class OrderAdmin(admin.ModelAdmin):
    list_display = ('coffee', 'quantity', 'total_price')
    search_fields = ('coffee__name',)
    list_filter = ('coffee',)

# Register models with the admin site
admin.site.register(CoffeeType, CoffeeTypeAdmin)
admin.site.register(Order, OrderAdmin)
