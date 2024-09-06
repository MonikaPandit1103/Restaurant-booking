from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'dob', 'age', 'married', 'gender', 'location']
    list_filter = ['location', 'age']
    search_fields = ['name', 'email']

admin.site.register(Customer, CustomerAdmin)

# Register your models here.
