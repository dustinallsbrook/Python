from operations import resources
from operations import MENU
cash_balance = 0


def main():
    initiation = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # os.system("clear")
    if initiation == "off":
        exit()
    elif initiation ==  "espresso" or initiation == "latte" or initiation == "cappuccino":
        check_coffee(initiation)
    elif initiation == "report":
        report()
        main()
    else:
        exit()
    check_money(initiation)
    make_coffee(initiation)
    main()


def check_coffee(initiation):
    for key in resources:
        if key in MENU[initiation]["ingredients"]:
            if resources[key] < MENU[initiation]["ingredients"][key]:
                print(f"Not enough {key}. Please make another selection.")
                main()


def check_money(initiation):
    global cash_balance
    price = MENU[initiation]["cost"]
    print("Please insert coins")
    coins = {"quarters":0, "dimes":0, "nickles":0, "pennies":0}
    for i in coins:
        coins[i] = int(input(f"How many {i}?: "))
    supplied = (.25 * coins["quarters"]) + (.1 * coins["dimes"]) + (.05 * coins["nickles"]) + (.01 * coins["pennies"])
    if supplied < price:
        print("Sorry, not enough coins. Money refunded.")
        exit()
    # print("1")
    # report()
    cash_balance += MENU[initiation]["cost"]
    change = supplied - MENU[initiation]["cost"]
    print(f"Here is ${float(change):.2f} in change.")


def make_coffee(initiation):
    for key in MENU[initiation]["ingredients"]:
        resources[key] = resources[key] - MENU[initiation]["ingredients"][key]
    print(f"Here is your {initiation}. Enjoy!")
    # print("2")
    # report()


def report():
    for key in resources:
        # print(key)
        print(f"There is {resources[key]}ml of {key} remaining")
    print(f"The is a balance of ${cash_balance:.2f}.")


main()

