from django.db import models

# Create your models here.

class TourPackage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='tour_images/')

    def __str__(self):
        return self.title

class Itinerary(models.Model):
    tour_package = models.ForeignKey(TourPackage, related_name='itineraries', on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    transportation = models.CharField(max_length=200)
    attractions = models.TextField()

    def __str__(self):
        return f"{self.tour_package.title} - Day {self.day_number}"
