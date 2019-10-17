from django.db import models

# Create your models here.
class Serving(models.Model):
    size = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.size}"

class Category(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"

class Topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"

class Menu(models.Model):
    fooditem = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="food")
    price = models.DecimalField(decimal_places=2, max_digits=4)
    size = models.ForeignKey(Serving, on_delete=models.CASCADE, related_name="serving")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")

    def __str__(self):
        return f"{self.category}: {self.fooditem} {self.size}  => {self.price}"

class Order(models.Model):
    order = models.ManyToManyField(Menu, blank=True, related_name="orders")

    def __str__(self):
        return f"Order made: {Menu.fooditem} -> {Menu.price}"


# class Subs(models.Model):
#     food = models.CharField(max_length=64)
#     small = models.DecimalField(decimal_places=2, max_digits=4)
#     large = models.DecimalField(decimal_places=2, max_digits=4)
#
#     def __str__(self):
#         return f"{self.food}: Small => {self.small}  Large => {self.large}"

# class Pasta(models.Model):
#     food = models.CharField(max_length=64)
#     price = models.DecimalField(decimal_places=2, max_digits=4)
#
#     def __str__(self):
#         return f"{self.food}: Price => {self.price}"
#
# class Salads(models.Model):
#     food = models.CharField(max_length=64)
#     price = models.DecimalField(decimal_places=2, max_digits=4)
#
#     def __str__(self):
#         return f"{self.food}: Price => {self.price}"
