from django.contrib import admin
from .models import TourPackage, Itinerary

# Register your models here.

class ItineraryInline(admin.TabularInline):
    model = Itinerary
    extra = 1

class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'duration')
    inlines = [ItineraryInline]

admin.site.register(TourPackage, TourPackageAdmin)
