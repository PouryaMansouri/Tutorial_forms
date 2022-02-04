from django.contrib import admin

# Register your models here.
from customers.forms import CustomerForm
from customers.models import Customer, Car, Club


class CarInline(admin.StackedInline):
    model = Car
    extra = 1


class ClubInline(admin.TabularInline):
    model = Club
    extra = 2


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForm
    list_display = ['id', 'name', 'status', 'email', 'phone', 'count_club']
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
    search_fields = ['name', 'phone']

    def change_status(self, request, queryset):
        queryset.update(status=True)

    actions = ['change_status']

    # def count_car(self, obj: Customer):
    #     return obj.car_set.count()

    def count_club(self, obj: Customer):
        return obj.club_set.count()

    # count_car.short_description = "cars"


class CarAdmin(admin.ModelAdmin):
    list_display = ['customer', 'car_name', 'price']

    list_filter = ['customer', 'price']
    search_fields = ['customer__name', 'customer__phone']
    autocomplete_fields = ['customer', ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Club)
