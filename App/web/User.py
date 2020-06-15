import PaymentInfo, datetime, shelve

class User:

    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__addresses = {}
        self.__address_selected = ""
        self.__paymentInfo = {}
        self.__payment_selected = ""
        self.__date = datetime.datetime.now().strftime("%d") + ' ' + datetime.datetime.now().strftime("%b")

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_orders(self):
        return self.__orders

    def get_addresses(self):
        return self.__addresses

    def get_address_selected(self):
        return self.__address_selected

    def get_payment_info(self):
        return self.__paymentInfo
    
    def get_date(self):
        return self.__date

    def get_payment_selected(self):
        return self.__payment_selected

    def set_username(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_orders(self, orders):
        self.__orders = orders

    def set_addresses(self, address):
        self.__addresses = address

    def set_address_selected(self, value):
        self.__address_selected = value

    def set_payment_info(self, value):
        self.__paymentInfo = value

    def set_payment_selected(self, value):
        self.__payment_selected = value
