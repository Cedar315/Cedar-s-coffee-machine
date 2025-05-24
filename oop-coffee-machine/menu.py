class MenuItem:
    def __init__(self,name,cost,water,milk,coffee):
        """
        attributes for every drink
        """
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water" : water,
            "milk": milk,
            "coffee": coffee
        }
class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=5.0),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=4.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=5.5),
            MenuItem(name="flat white", water=180, milk=150, coffee=24, cost=5.0),
            MenuItem(name="mocha", water=200, milk=150, coffee=24, cost=6.0),
            MenuItem(name="long black", water=250, milk=0, coffee=24, cost=4.5),
            MenuItem(name="hot chocolate", water=200, milk=150, coffee=0, cost=5.5)
        ]
    def get_item(self):
        """
        show the whole menu(name of drinks) to the user
        """
        options =""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self,order_name):
        """
        find the order from the menu, check if it exists
        """
        for item in self.menu:
            if order_name == item.name:
                return item
        #if item noy in self.menu
        # print("sorry we don't have it")
        return False

