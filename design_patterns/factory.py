""" Factory Design patterns are useful in creating objects at runtime. """

from abc import ABCMeta, abstractclassmethod


class IPerson(metaclass=ABCMeta):
    """ Cannot be instantiated """

    @abstractclassmethod
    def person_method(self):
        """ Interface method """


class Student(IPerson):
    def __init__(self):
        self.name = "A student!"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):
    def __init__(self):
        self.name = "A teacher!"

    def person_method(self):
        print("I am a teacher")


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()

        print("Invalid Input")
        return -1


if __name__ == "__main__":
    choice = input("Type of person??\n")
    person = PersonFactory.build_person(choice)
    person.person_method()
