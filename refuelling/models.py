from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Refuel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    distance_km = models.PositiveIntegerField()
    petrol_amount_litre = models.PositiveIntegerField()
    refuel_date = models.DateTimeField()
    
    def __str__(self):
        return f"Username: {self.user.username} | Refuel date: {self.refuel_date}"