from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# carModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

class CarMakeInline(admin.StackedInline):
    model = CarMake

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)