
class Student:

    def __init__(self, id, name, age, course, email, phone):

        self.__id = id
        self.__name = name
        self.__age = age
        self.__course = course
        self.__email = email
        self.__phone = phone

    # Getters

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_course(self):
        return self.__course

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    # Setters

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_course(self, course):
        self.__course = course

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone
