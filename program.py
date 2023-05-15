class Pizza:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

class Drink:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

def place_order(pizzas, drinks):
    print("Menu:")
    print("Pizzas:")
    for i, pizza in enumerate(pizzas):
        print(f"{i+1}. {pizza.name} - {pizza.price} грн")
    print("Drinks:")
    for i, drink in enumerate(drinks):
        print(f"{i+1}. {drink.name} - {drink.price} грн")

    order_total = 0
    pizza_choice = input("Введіть номер піци: ")
    if pizza_choice.isdigit():
        pizza_index = int(pizza_choice) - 1
        if 0 <= pizza_index < len(pizzas):
            selected_pizza = pizzas[pizza_index]
            order_total += selected_pizza.price
            print(f"Ви обрали піцу: {selected_pizza.name}")
        else:
            print(f"Недійсний вибір піци: {pizza_choice}")
    else:
        print(f"Недійсний вибір піци: {pizza_choice}")

    drink_choice = input("Введіть номер напою: ")
    if drink_choice.isdigit():
        drink_index = int(drink_choice) - 1
        if 0 <= drink_index < len(drinks):
            selected_drink = drinks[drink_index]
            order_total += selected_drink.price
            print(f"Ви обрали напій: {selected_drink.name}")
        else:
            print(f"Недійсний вибір напою: {drink_choice}")
    else:
        print(f"Недійсний вибір напою: {drink_choice}")

    print(f"Загальна вартість замовлення: {selected_pizza.name} {selected_drink.name} {order_total} грн")

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
