from datetime import datetime
import json
from customer import Customer
from shop import Shop


def shop_trip() -> None:
    with open("app\config.json", "r") as file:
        config = json.load(file)

    shops_list = [Shop(shop) for shop in config["shops"]]
    customers_list = [Customer(person) for person in config["customers"]]
    for person in customers_list:
        print(f"{person.name} has {person.money} dollars")

        choosing = {}
        for shop in shops_list:
            choosing[shop]: person.total_cost(person, shop, config["FUEL_PRICE"])
            print(f"{person.name}'s trip to the {shop.name} costs {choosing[shop]}")

        cheapest = min(choosing)
        if choosing[cheapest] < person.money:
            person.trip_info(cheapest, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            person.money -= choosing[cheapest]
            print(f"{person.name} now has {person.money} dollars")
