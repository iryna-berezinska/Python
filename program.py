class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Pizza(Food):
    def __init__(self, name, ingredients, price):
        super().__init__(name, price)
        self.ingredients = ingredients

class Drink(Food):
    def __init__(self, name, description, price):
        super().__init__(name, price)
        self.description = description

def print_menu(pizzas, drinks):
    print("Menu:")
    print("Pizzas:")
    for i, pizza in enumerate(pizzas):
        print(f"{i+1}. {pizza.name} - {pizza.price} грн")
    print("Drinks:")
    for i, drink in enumerate(drinks):
        print(f"{i+1}. {drink.name} - {drink.price} грн")

def order_pizza(pizzas):
    pizza_choice = input("Введіть номер піци: ")
    if pizza_choice.isdigit():
        pizza_index = int(pizza_choice) - 1
        if 0 <= pizza_index < len(pizzas):
            selected_pizza = pizzas[pizza_index]
            print(f"Ви обрали піцу: {selected_pizza.name}")
            return selected_pizza
        else:
            print(f"Недійсний вибір піци: {pizza_choice}")
    else:
        print(f"Недійсний вибір піци: {pizza_choice}")
    return None

def order_drink(drinks):
    order_total = 0
    drink_choice = input("Введіть номер напою: ")
    if drink_choice.isdigit():
        drink_index = int(drink_choice) - 1
        if 0 <= drink_index < len(drinks):
            selected_drink = drinks[drink_index]
            order_total += selected_drink.price
            print(f"Ви обрали напій: {selected_drink.name}")
            return selected_drink
        else:
            print(f"Недійсний вибір напою: {drink_choice}")
    else:
        print(f"Недійсний вибір напою: {drink_choice}")
    return None

def print_order(pizza, drink):
    if pizza and drink:
        order_total = pizza.price + drink.price
        print(f"Загальна вартість замовлення: {order_total} грн")
        print(f"Піца: {pizza.name}")
        print(f"Напій: {drink.name}")

def place_order(pizzas, drinks):
    print_menu(pizzas, drinks)
    selected_pizza = order_pizza(pizzas)
    selected_drink = order_drink(drinks)
    print_order(selected_pizza, selected_drink)

if __name__ == "__main__":
    pizzas = [
        Pizza("Маргарита", "сир, томати, базилік", 300),
        Pizza("Пепероні", "сир, пепероні", 320),
        Pizza("Гавайська", "сир, шинка, ананаси", 310)
    ]

    drinks = [
        Drink("Кола", "газований напій", 50),
        Drink("Сік", "природний сік", 60),
        Drink("Вода", "мінеральна вода", 30)
    ]

    place_order(pizzas, drinks)
