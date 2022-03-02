
class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def increase_wallet(self, amount):
        self.wallet += amount

    def customer_can_afford(self, price):
        self.can_afford = False
        if self.wallet >= price:
            self.can_affrod = True
        return self.can_afford