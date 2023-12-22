from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

eog = False
menu= Menu()
coffee_maker= CoffeeMaker()
money_machine= MoneyMachine()

while eog == False:
    ask = input(f"What do you want {menu.get_items()}: ")

    if ask == "report":
        coffee_maker.report()
        money_machine.report()
    elif ask== "off":
        eog= True
    else:
        ask_menu_item_obj= menu.find_drink(ask)
        if coffee_maker.is_resource_sufficient(ask_menu_item_obj) and money_machine.make_payment(ask_menu_item_obj.cost):
            coffee_maker.make_coffee(ask_menu_item_obj)