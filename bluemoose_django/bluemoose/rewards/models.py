from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)  # Add this line for phone number
    reward_balance = models.IntegerField(default=0)
    past_purchases = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
