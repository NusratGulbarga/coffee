from django.db import models

class CoffeeType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='coffee_images/', null=True, blank=True)  # Add this line


    def __str__(self):
        return self.name

class Order(models.Model):
    coffee = models.ForeignKey(CoffeeType, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)  # Added customer name
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer_name} - {self.coffee.name}"
    def save(self, *args, **kwargs):
        self.total_price = self.coffee.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order of {self.quantity} {self.coffee.name}"


