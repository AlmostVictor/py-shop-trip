from math import dist
from shop import Shop


class Customer:
    def __init__(self, person_dict: dict) -> None:
        self.name = person_dict["name"]
        self.product_cart = person_dict["product_cart"]
        self.coords = person_dict["location"]
        self.money = person_dict["money"]
        self.fuel_for_1_km = person_dict["car"]["fuel_consumption"] / 100

    def total_cost(self, shop: Shop, fuel_price: float) -> float:
        fuel_cost = (round(dist(shop.coords, self.coords), 2) *
                     self.fuel_for_1_km * fuel_price * 2)
        return fuel_cost + shop.purchase_receipt(self.product_cart)[0]

    def trip_info(self, shop: Shop, date: str) -> None:
        print(f"{self.name} rides to {shop.name}\n\n"
              f"Date: {date}"
              f"Thanks, {self.name}, for your purchase!"
              "You have bought:")
        cheque = shop.purchase_receipt(self.product_cart)
        for product, amount in cheque[1].items():
            print(f"{amount[0]} {product}s for {amount[1]} dollars")
        print(f"Total cost is {cheque[0]}"
              "See you again!\n\n"
              f"{self.name} rides home")
