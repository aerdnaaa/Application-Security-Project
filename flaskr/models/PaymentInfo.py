import uuid
class PaymentInfo:
    def set_id(self):
        while True:
            id = str(uuid.uuid4())
            if id[0] in '1234567890':
                id = str(uuid.uuid4())
            else:
                break
        self.__id = id
    
    def __init__(self, creditCardNo="", expiryMonth="", expiryYear="", ccv="", cardName=""):
        self.set_id()
        self.__creditCardNo = creditCardNo
        self.__cardName = cardName
        self.__ccv = ccv
        self.__expiryMonth = expiryMonth
        self.__expiryYear = expiryYear

    def get_id(self):
        return self.__id

    def get_credit_card_number(self):
        return self.__creditCardNo

    def get_card_name(self):
        return self.__cardName

    def get_ccv(self):
        return self.__ccv

    def get_expiry_month(self):
        return self.__expiryMonth

    def get_expiry_year(self):
        return self.__expiryYear

    def set_credit_card_number(self, value):
        self.__creditCardNo = value

    def set_card_name(self, value):
        self.__cardName = value

    def set_ccv(self, value):
        self.__ccv = value

    def set_expiry_month(self, value):
        self.__expiryMonth = value

    def setExpiryYear(self, value):
        self.__expiryYear = value