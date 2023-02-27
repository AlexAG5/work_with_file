# ЗАДАНИЕ №1
from pprint import pprint


def get_cook_book():
    with open('recipes.txt') as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            ingredients_count = int(file.readline())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient = file.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish] = ingredients
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    recipes = get_cook_book()
    dishes_dict = {}
    for dish in dishes:
        if dish in recipes:
            for ingredient in recipes[dish]:
                if ingredient["ingredient_name"] in dishes_dict:
                    dishes_dict[ingredient["ingredient_name"]]["quantity"] += (int(ingredient["quantity"]) * person_count)
                else:
                    dishes_dict.setdefault(ingredient["ingredient_name"], {"quantity": (int(ingredient["quantity"]) * person_count), "measure": ingredient["measure"]})
        else:
            print("Ошибка")
    return dishes_dict


def main():
    print("1 - Задание №1. Поваренная книга.", "2 - Задание №2. Расчёт ингредиентов по количеству персон.", sep="; ")
    command = input("Введите команду: ")
    if command == "1":
        pprint(get_cook_book())
    elif command == "2":
        dish = input("Название блюд: ").split(", ")
        persons = int(input("Введите количество персон: "))
        pprint(get_shop_list_by_dishes(dish, persons))
    else:
        pprint("Ошибка")


main()