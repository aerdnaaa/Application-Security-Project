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
        self.__expiryMonth = expiryMonth
        self.__expiryYear = expiryYear
        self.__ccv = ccv
        self.__cardName = cardName

    def get_id(self):
        return self.__id

    def getCreditCardNo(self):
        return self.__creditCardNo

    def setCreditCardNo(self, value):
        self.__creditCardNo = value

    def getExpiryMonth(self):
        return self.__expiryMonth

    def setExpiryMonth(self, value):
        self.__expiryMonth = value

    def getExpiryYear(self):
        return self.__expiryYear

    def setExpiryYear(self, value):
        self.__expiryYear = value

    def getCcv(self):
        return self.__ccv

    def setCcv(self, value):
        self.__ccv = value

    def getCardName(self):
        return self.__cardName

    def setCardName(self, value):
        self.__cardName = value
