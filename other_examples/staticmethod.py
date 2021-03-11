""" staticmethod decorators are useful when a function of a class is needed without making an
    instance. Makes code more readable!

    No self keyword is passed while declaring a static function.
"""


class Person:
    @staticmethod
    def compute_age(age):
        if age > 18:
            print("Adult")
        else:
            print("Child")


Person.compute_age(23)  # compute_age is a static function. No object creation needed!

