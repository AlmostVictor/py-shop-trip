class Shop:
    def __init__(self, shop_dict: dict) -> None:
        self.name = shop_dict["name"]
        self.coords = shop_dict["location"]
        self.products = shop_dict["products"]

    def purchase_receipt(self, product_cart: dict) -> tuple:
        total = 0
        products_cost = {}
        for product in product_cart.keys():
            cost = product_cart[product] * self.products[product]
            products_cost[product] = (product_cart[product], cost)
            total += cost
        return total, products_cost
