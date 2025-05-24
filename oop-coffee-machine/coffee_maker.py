class CoffeeMaker:
    def __init__(self):
        self.resources ={
            "water": 3000,
            "milk":2000,
            "coffee":1000
            #since they are raw materials we don't need to change their values externally
        }

    def report(self):
        """
        show remaining materials in the coffee machine
        """
        print(f"water:{self.resources["water"]}ml")
        print(f"milk:{self.resources["milk"]}ml")
        print(f"coffee:{self.resources["coffee"]}g")

    def is_resource_sufficient(self,drink):
        """
        check if the resources is sufficient
        """
        #remenber there are 3 resources
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self,order):
        for item in order.ingredients:
            self.resources[item]-=order.ingredients[item]
        print(f"here is your {order.name},enjoy")
