""" Singleton is useful if the class is to be instantiated just once! """

from abc import ABCMeta, abstractclassmethod


class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def print_data():
        """ Pass """


class PersonSingleton(IPerson):
    __instance = None  # Pvt. variable set to None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name="Aniket", age=25):
        if PersonSingleton.__instance != None:
            try:
                raise Exception
            except Exception as e:
                print("Exception: Not happening")

        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(
            f"Name: {PersonSingleton.__instance.name}\nAge: {PersonSingleton.__instance.age}"
        )


p = PersonSingleton("Mike", 30)
p.print_data()

p1 = PersonSingleton()  # This will fail
