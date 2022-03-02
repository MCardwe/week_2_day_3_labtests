import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Gerald", 10)


    def test_customer_has_name(self):
        self.assertEqual("Gerald",self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    def test_increase_wallet(self):
        self.customer.increase_wallet(2.50)
        excepted = 12.50
        actual = self.customer.wallet
        self.assertEqual(excepted, actual)

    def test_decrease_wallet(self):
        self.customer.increase_wallet(-2.50)
        excepted = 7.50
        actual = self.customer.wallet
        self.assertEqual(excepted, actual)

    def test_can_customer_afford(self):
        drink_price = self.pub.drinks[0]["price"]
        can_he_afford = self.customer.can_afford(drink_price)
        self.assertEqual(True, can_he_afford)

    def test_customer_can_buy_drink(self):
        pass
