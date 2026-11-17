class BankAccount:

    def __init__(self,account_no,name,age,address,phone,email,balance):
        self.__account_no = account_no
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__balance = balance


# Gettters
    def get_account_no(self):
        return self.__account_no

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_balance(self):
        return self.__balance


# Setters

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def set_address(self,address):
        self.__address = address

    def set_phone(self,phone):
        self.__phone = phone

    def set_email(self,email):
        self.__email = email
