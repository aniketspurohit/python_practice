""" This pattern is useful if a tree like heirarchy is needed."""

from abc import ABCMeta, abstractstaticmethod, abstractmethod


class IDept(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        """ To be implemented in child class"""

    @abstractstaticmethod
    def print_dept():
        """ To be implemented in child class"""


class Accounting(IDept):
    def __init__(self, employees):
        self.employees = employees

    def print_dept(self):
        print(f"Acc:{self.employees}")


class Development(IDept):
    def __init__(self, employees):
        self.employees = employees

    def print_dept(self):
        print(f"Dev:{self.employees}")


class Parent(IDept):
    def __init__(self, employees=30):
        self.employees = employees
        self.base_employees = employees
        self.sub_dept = []

    def add(self, dept):
        self.sub_dept.append(dept)
        self.employees += dept.employees

    def print_dept(self):
        print(f"Parent: {self.base_employees}")
        for i in self.sub_dept:
            i.print_dept()
        print(f"Total: {self.employees}")


d1 = Accounting(23)
d2 = Development(34)

parent_dept = Parent()  # initial value set to 30
parent_dept.add(d1)
parent_dept.add(d2)

parent_dept.print_dept()
