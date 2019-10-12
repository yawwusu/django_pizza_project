from django.db import models

# Create your models here.
class Regular(models.Model):
    food = models.CharField(max_length=64)
    small = models.DecimalField(decimal_places=2, max_digits=4)
    large = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.food}: Small => {self.small}  Large => {self.large}"

class Silician(models.Model):
    food = models.CharField(max_length=64)
    small = models.DecimalField(decimal_places=2, max_digits=4)
    large = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.food}: Small => {self.small}  Large => {self.large}"

class Toppings(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"

class Subs(models.Model):
    food = models.CharField(max_length=64)
    small = models.DecimalField(decimal_places=2, max_digits=4)
    large = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.food}: Small => {self.small}  Large => {self.large}"

class Pasta(models.Model):
    food = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.food}: Price => {self.price}"

class Salads(models.Model):
    food = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.food}: Price => {self.price}"

class DinnerPlatters(models.Model):
    food = models.CharField(max_length=64)
    small = models.DecimalField(decimal_places=2, max_digits=4)
    large = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.food}: Small => {self.small}  Large => {self.large}"
