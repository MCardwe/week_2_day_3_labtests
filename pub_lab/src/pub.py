from optparse import AmbiguousOptionError
from traceback import print_exception


class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def count_drinks(self):
        return len(self.drinks)

   
    def add_drink(self,name,price):
        new_drink = {
            "name" : name,
            "price" : price
        }

        self.drinks.append(new_drink)

    def remove_drink(self, name):
        drink_to_remove = self.find_drink_by_name(name)
        
        for drink in self.drinks:
            if drink == drink_to_remove:
                self.drinks.remove(drink)

    def is_stock_empty(self):
        if self.count_drinks() == 0:
            return True
        else:
            return False

    def find_drink_by_name(self, name):

        for drink in self.drinks:
            if drink["name"] == name:
                return drink
