from django.contrib import admin
from .models import Category, Sport
# Register your models here.

class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'created')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'created')

    list_display_links = ('name',)
admin.site.register(Category)
admin.site.register(Sport, SportAdmin)
