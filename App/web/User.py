from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, username, email, password):
        self.id = id
        self.__username = username
        self.__email = email
        self.__password = password

    def get_username(self):
        return self.__username
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password


    def set_email(self, email):
        self.__email = email
    def set_password(self, password):
        self.__password = password

    
