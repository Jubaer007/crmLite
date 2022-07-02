from django.contrib import admin
from . import models

class OrderView(admin.ModelAdmin):
    list_display = ('customer', 'product', 'date_created', 'status')

class CustomerView(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date_created' )

admin.site.register(models.Customer, CustomerView)
admin.site.register(models.Product)
admin.site.register(models.Order, OrderView)
admin.site.register(models.Tag)


