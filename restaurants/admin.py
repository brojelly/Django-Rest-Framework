from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact', 'open_time', 'close_time', 'regular_holiday')
    search_fields = ('name', 'address')

