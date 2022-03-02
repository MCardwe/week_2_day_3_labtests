from ast import excepthandler
import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub.drinks = [
            {
                "name" : "beer",
                "price" : 3.50
            },
            {
                "name" : "cider",
                "price": 2.50
            }
        ]

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name) 

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        excepted = 102.50
        actual = self.pub.till
        self.assertEqual(excepted, actual)

    def test_decrease_till(self):
        self.pub.increase_till(-2.50)
        self.assertEqual(97.5, self.pub.till)

    def test_count_drinks(self):
        amount_of_drinks = self.pub.count_drinks()
        self.assertEqual(2, amount_of_drinks)
    
   
    def test_can_add_drink(self):
        self.pub.add_drink("wine", 5)
        self.assertEqual(3, self.pub.count_drinks())

    def test_can_find_by_name(self):
        self.pub.add_drink("wine", 5)
        drink = self.pub.find_drink_by_name("wine")
        self.assertEqual(self.pub.drinks[2], drink)
        
    def test_is_stock_not_empty(self):
        self.assertEqual(False, self.pub.is_stock_empty())

    
    def test_is_stock_empty(self):
        self.pub.drinks.clear()
        self.assertEqual(True, self.pub.is_stock_empty())

    def test_remove_drink(self):
        self.pub.remove_drink("beer")
        self.assertEqual(self.pub.count_drinks(), 1)