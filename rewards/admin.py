from django.contrib import admin
from .models import Customer, RedeemableItem, PurchasableItem, Order

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')


admin.site.register(RedeemableItem)
admin.site.register(PurchasableItem)
admin.site.register(Order)

