class MoneyMachine:

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }


    def __init__(self):
        self.money_received = 0
        self.card_balance = 10.0 # initial balance

    def process_coins(self):
        """
        ask user entering the money
        """
        print("please enter the money")
        for coin in self.COIN_VALUES:
            # coin is the key in dictionary Coinvalue
            numbers = int(input(f"how many {coin}:")) #change str to int
            self.money_received += numbers * self.COIN_VALUES[coin]
        print(f"you entered ${self.money_received}.")
        return self.money_received

    def make_payment(self,order):
        """
        compare with the cost of coffee, check if it is a smooth transaction
        give the change to the user
        """
        if self.money_received >= order.cost:
            change = round (self.money_received-order.cost,2)
            print(f"here is your change : ${change}")
            return True
        else:
            print("sorry that's not enough money.Money refund")


    def make_card_payment(self,drink):
        if self.card_balance >= drink.cost:
            self.card_balance -= drink.cost
            print(f"Payment successful. Remaining card balance: ${self.card_balance:.2f}")
            return True
        else:
            print(f"Insufficient card balance. You have ${self.card_balance:.2f}, but need ${drink.cost:.2f}.")
            return False

    def top_up_card(self):
        print(f"Your current card balance is: ${self.card_balance:.2f}")
        amount = float(input("Enter the amount to top up your card: $"))
        if amount <= 0:
            print("Invalid top-up amount. Please enter a positive number.")
        else:
            self.card_balance += amount
            print(f"Top-up successful! New balance: ${self.card_balance:.2f}")
