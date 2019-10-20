from django.db.models import Max
from django.test import Client, TestCase

from .models import Serving, Category, Menu, Topping, Order

# Create your tests here.
class OrdersTestCase(TestCase):

    def setUp(self):

        # Create categories.
        c1 = Category.objects.create(type="Cat1")
        c2 = Category.objects.create(type="Cat2")

        # Create sizes.
        s1 = Serving.objects.create(size="Size1")
        s2 = Serving.objects.create(size="Size2")

        # Create toppings/extras.
        t1 = Topping.objects.create(topping="Add1")
        t2 = Topping.objects.create(topping="Add2")

        # Create Menus.
        Menu.objects.create(fooditem=t1, price=23.23, size=s1, category=c1)
        Menu.objects.create(fooditem=t2, price=25.00, size=s2, category=c2)


    def test_food_count(self):
        a = Menu.objects.get(topping="Add1")
        self.assertEqual(a.food.count(), 1)

    def test_serving_count(self):
        a = Menu.objects.get(size="Size2")
        self.assertEqual(a.serving.count(), 1)

    def test_category_count(self):
        a = Menu.objects.get(category="Cat1")
        self.assertEqual(a.category.count(), 1)

    # def test_valid_Order(self):
    #     a1 = Menu.objects.get(code="AAA")
    #     a2 = Menu.objects.get(code="BBB")
    #     o = Order.objects.get(origin=a1, destination=a2)
    #     self.assertTrue(f.is_valid_Order())
    #
    # def test_invalid_Order_destination(self):
    #     a1 = Menu.objects.get(code="AAA")
    #     o = Order.objects.get(origin=a1, destination=a1)
    #     self.assertFalse(f.is_valid_Order())
    #
    # def test_invalid_Order_duration(self):
    #     a1 = Menu.objects.get(code="AAA")
    #     a2 = Menu.objects.get(code="BBB")
    #     o = Order.objects.get(origin=a1, destination=a2)
    #     f.duration = -100
    #     self.assertFalse(f.is_valid_Order())
    #
    # def test_index(self):
    #     c = Client()
    #     response = c.get("/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.context["Orders"].count(), 2)
    #
    # def test_valid_Order_page(self):
    #     a1 = Menu.objects.get(code="AAA")
    #     o = Order.objects.get(origin=a1, destination=a1)
    #
    #     c = Client()
    #     response = c.get(f"/{f.id}")
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_invalid_Order_page(self):
    #     max_id = Order.objects.all().aggregate(Max("id"))["id__max"]
    #
    #     c = Client()
    #     response = c.get(f"/{max_id + 1}")
    #     self.assertEqual(response.status_code, 404)
    #
    # def test_Order_page_menuitems(self):
    #     o = Order.objects.get(pk=1)
    #     p = menuitem.objects.create(first="Alice", last="Adams")
    #     f.menuitems.add(p)
    #
    #     c = Client()
    #     response = c.get(f"/{f.id}")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.context["menuitems"].count(), 1)
    #
    # def test_Order_page_non_menuitems(self):
    #     o = Order.objects.get(pk=1)
    #     p = menuitem.objects.create(first="Alice", last="Adams")
    #
    #     c = Client()
    #     response = c.get(f"/{f.id}")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.context["non_menuitems"].count(), 1)
