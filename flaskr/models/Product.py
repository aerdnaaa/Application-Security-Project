class Product:
    def __init__(self, name, selling_price, cost_price):
        self.__name = name
        self.__selling_price = selling_price
        self.__cost_price = cost_price

    def get_name(self):
        return self.__name

    def get_selling_price(self):
        return self.__selling_price

    def get_cost_price(self):
        return self.__cost_price
