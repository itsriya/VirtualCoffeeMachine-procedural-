"""
the functions:
coffee(): to make coffee by adding water milk and coffee
report(): to print the amount of water, milk and coffee
calculate(): to calculate and print the price of coffee and change returned. the machine is coin operated.
              if the money is not enough take back the used quantity of water milk and coffee.
the machine is coin operated.
quarter=$0.25
penny=$0.01
nickel=$0.05
dime=$0.10
price of espresso: $1.50
price of latte:$2.50
price of cappuccino:$3.0
espresso=50ml of water; 18 gm of coffee
latte=200 ml of water ; 24 gm of coffee; 100 ml of milk
cappuccino=250 ml of water; 24 gm of coffee;150 ml of milk
"""


water = 500
coffee = 100
milk = 500


def coffee_machine(arg1):
    global water
    global milk
    global coffee
    if arg1 == 'espresso':
        if water > 50 and coffee > 18:
            y = calculate('espresso')
            if y == 1:
                water = water-50
                coffee = coffee-18
                print(f"Enjoy your {arg1}")
            else:
                print("Did not pay enough")
        else:
            print("Not enough quantities")
    elif arg1 == 'latte':
        if water < 200 or coffee < 24 or milk < 100:
            print("Not enough quantity")

        else:
            y = calculate('latte')
            if y == 1:
                water = water-200
                coffee = coffee-24
                milk = milk-100
                print(f"Enjoy your{arg1}")
            else:
                print("Did not pay enough")
    elif arg1 == 'cappuccino':
        if water < 250 or coffee < 24 or milk < 150:
            print("Out of quantity")
        else:
            y = calculate('cappuccino')
            if y == 1:
                water = water-250
                coffee = coffee-24
                milk = milk - 50
                print(f"Enjoy your {arg1}")
            else:
                print("Did not pay enough")


def report():
    print(f"Water:{water}")
    print(f"coffee:{coffee}")
    print(f"milk:{milk}")


def calculate(arg2):
    quarter = int(input("Quarter:"))
    penny = int(input("Penny:"))
    dime = int(input("Dime:"))
    nickel = int(input("Nickel:"))
    total = quarter*0.25+nickel*0.05+dime*0.10+penny*0.01
    if arg2 == 'espresso' and total > 1.50 or total == 1.50:
        print(f"Your change is $ {round((total-1.5),2)}")
        return 1
    elif arg2 == 'latte' and total > 2.50 or total == 2.50:
        print(f"Your change $ {round((total-2.5),2)}")
        return 1
    elif arg2 == 'cappuccino' and total > 3.0 or total == 3.0:
        print(f"Your change is $ {round((total-3.0),2)}")
        return 1
    else:
        return 0


def main():
    while 1:
        user_input = input("What would you like to have(Espresso/Latte/Cappuccino)?").lower()
        if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
            coffee_machine(user_input)
        elif user_input == 'report':
            report()
        elif user_input == 'exit':
            break


main()
