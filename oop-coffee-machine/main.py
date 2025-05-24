from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu=Menu()
coffee_maker=CoffeeMaker()
money_machine = MoneyMachine()

def show_menu(menu):
    print("\n=== Cedar’s Coffee Machine Menu ===")
    for idx, item in enumerate(menu.menu, 1):
        print(f"{idx}. {item.name.title()} (${item.cost:.2f})")
    print("r. View resource report")
    print("q. Quit\n")


#change it to a loop
is_on = True

while is_on:
    print("Kick off a great day—grab your coffee here!")
    show_menu(menu)

    while True:
        choice = input("Please select your drink by number, or type 'r' for report, 'q' to quit: ").strip().lower()
        if choice == "r":
            coffee_maker.report()
            continue  # stay in inner loop
        elif choice == "q":
            print("Have a nice day~")
            is_on = False
            break  # break out to exit
        elif choice.isdigit() and 1 <= int(choice) <= len(menu.menu):
            drink = menu.menu[int(choice) - 1]
            break  # valid input, proceed to payment
        else:
            print("Invalid choice, please try again.")  # NO print menu or welcome again!
            continue  # prompt again, don't print menu again

    if not is_on:
        break

    if not coffee_maker.is_resource_sufficient(drink):
        continue

    payment_method = input("How would you like to pay? (card/cash): ").lower()
    if payment_method == "card":
        if money_machine.make_card_payment(drink):
            coffee_maker.make_coffee(drink)
        else:
            topup_choice = input("Would you like to top up your card? (yes/no): ").lower()
            if topup_choice == "yes":
                money_machine.top_up_card()
                if money_machine.make_card_payment(drink):
                    coffee_maker.make_coffee(drink)
                else:
                    print("Still insufficient funds after top-up.")
                    continue
            else:
                print("Payment cancelled.")
                continue
    elif payment_method == "cash":
        money_machine.money_received = 0
        money_machine.process_coins()
        if money_machine.make_payment(drink):
            coffee_maker.make_coffee(drink)
        else:
            continue
    else:
        print("Invalid payment method. Please choose 'card' or 'cash'.")
        continue

    continue_choice = input("Would you like another coffee? (yes/no): ").lower()
    if continue_choice != "yes":
        print("Have a nice day!\n")
        break







