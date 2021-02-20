class Person:
    def __init__(self, name, age):
        self.__name = name  # __variable is a pvt. variable
        self.__age = age

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod
    def printing():
        print(
            "hello Aniket"
        )  # Static methods aren't related to class. Hence, no self is passed.


Person.printing()

p1 = Person("Aniket", 24)
print(p1.Name)

p1.printing()  # Prints the same value with/without initialisation

p1.name = "bob"
print(p1.name)  # possible due to setter function


"""
Note: __name is a private variable. This can't be accessed directly. Using @property will help access the variable.

Also, function overloading isn't defined in Python. Hence, @[getter function].setter is used to change the value.
"""

