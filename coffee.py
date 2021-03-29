import main
profit = 0
def is_coffee_possible(in_choice):
    for item in in_choice:
        if in_choice[item] >= main.resources[item]:
            print(f"Sorry not enough {item}")
            return False
        return True

def process_coins():
    total = int(input("number of quaters: $")) *0.25
    total+= int(input("number of dimes: ")) *0.10
    total+= int(input("number of nickles: $")) *0.05
    total += int(input("number of pennies: $")) *0.01
    return total

def is_transaction_success(money_paid, real_cost):
    if money_paid >= real_cost:
        change = round(money_paid - real_cost, 2)
        print(f"Here is your ${change} change")
        global profit
        profit += round(money_paid, 2)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        main.resources[item] -= order_ingredients[item]
        print(f'Here is your {drink_name}, Enjoy!')


is_off = True
while is_off == True:
    user_choice = input('What would you like? (espresso/latte/cappuccino): ')
    if user_choice == 'off':
        is_off = False
    elif user_choice == 'report':
        print("Here's the report")
        print(f"water :{main.resources['water']}ml")
        print(f"milk: {main.resources['milk']}ml")
        print(f"coffee: {main.resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = main.MENU[user_choice]
        if is_coffee_possible(drink['ingredients']):
            payment = process_coins()
            if is_transaction_success(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])








