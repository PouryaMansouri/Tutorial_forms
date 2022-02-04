from django.contrib import admin

# Register your models here.
from customers.models import Customer, Car, Club


class CarInline(admin.StackedInline):
    model = Car
    extra = 1


class ClubInline(admin.TabularInline):
    model = Club
    extra = 2


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone']
    list_display_links = ['email']
    # fields = ['name', 'phone']
    fieldsets = (
        ('General',
         {'fields': ['name', ]}),
        ('Info',
         {'fields': ['phone', 'email']}),
        ('Address',
         {'fields': ['address', ]}),
    )
    inlines = [CarInline, ClubInline]
    search_fields = ['name','phone']


class CarAdmin(admin.ModelAdmin):
    list_display = ['customer', 'car_name', 'price']

    list_filter = ['customer', 'price']
    search_fields = ['customer__name', 'customer__phone']
    autocomplete_fields = ['customer', ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Club)
